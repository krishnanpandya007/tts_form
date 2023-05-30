import os
import speech_recognition as sr
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from .models import Person
from .forms import AccountForm

# def home(request):
#     return render(request, 'index.html')

# def extract_text_from_audio(request):
#     if request.method == 'POST' and request.FILES.get('audioFile'):
#         audio_file = request.FILES['audioFile']

#         # Configure the speech recognizer
#         recognizer = sr.Recognizer()

#         try:
#             # Load the audio file
#             with sr.AudioFile(audio_file) as source:
#                 audio = recognizer.record(source)

#             # Extract text from audio
#             text = recognizer.recognize_google(audio)

#             # Return the extracted text as JSON response
#             return JsonResponse({'text': text}, status=200)

#         except sr.UnknownValueError:
#             return JsonResponse({'error': 'Unable to transcribe audio. Speech not recognized.'}, status=400)

#         except sr.RequestError:
#             return JsonResponse({'error': 'Unable to transcribe audio. Recognition service error.'}, status=500)

#     return JsonResponse({'error': 'Invalid request'}, status=400)


# def submit_form_api(request):
#     if request.method == 'POST':
#         form = AccountForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             city = form.cleaned_data['city']
#             district = form.cleaned_data['district']
#             mobile_number = form.cleaned_data['mobile_number']
            
#             user = Person(name=name, city=city, district=district, mobile_number=mobile_number)
#             user.save()

#             return JsonResponse({'success': True, 'message': 'Form submitted successfully'})
#         else:
#             errors = form.errors.as_json()
#             return JsonResponse({'success': False, 'errors': errors}, status=400)
#     else:
#         return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)



# import os
# import subprocess
# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotAllowed


# def index(request):
#     if request.method == 'POST':
#         audio_file = request.FILES['audio']

#         save_directory = 'tts_form/formfill'
#         os.makedirs(save_directory, exist_ok=True)

#         audio_path = os.path.join(save_directory, audio_file.name)
#         with open(audio_path, 'wb') as destination:
#             for chunk in audio_file.chunks():
#                 destination.write(chunk)

#         mp3_file = os.path.splitext(audio_path)[0] + '.mp3'
#         command = f'ffmpeg -i "{audio_path}" -acodec libmp3lame -b:a 128k "{mp3_file}"'
#         subprocess.call(command, shell=True)

#         return render(request, 'index.html')

#     return render(request, 'index.html')


import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed


def index(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio']

        save_directory = 'tts_form/formfill'
        os.makedirs(save_directory, exist_ok=True)

        audio_path = os.path.join(save_directory, audio_file.name)
        with open(audio_path, 'wb') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)
            return render(request, 'index.html')

    return render(request, 'index.html')


def mockform(request):
    if request.method == 'POST':
        audio_file = request.FILES['audioFile']
        audioField = request.GET.get('audioField', '') # name | city | district | phone
        preValues = {
            'name': request.POST.get('name', ''),
            'city': request.POST.get('city', ''),
            'district': request.POST.get('district', ''),
            'phone': request.POST.get('phone', ''),
        }
        # preName = request.GET.get('name', '')
        # preCity = request.GET.get('city', '')
        # preDistrict = request.GET.get('district', '') 
        # prePhone = request.GET.get('phone', '') 

        # Configure the speech recognizer
        recognizer = sr.Recognizer()

        try:
            # Load the audio file
            with sr.AudioFile(audio_file) as source:
                audio = recognizer.record(source)

            # Extract text from audio
            text = recognizer.recognize_google(audio)

            preValues[audioField] = text

            return render(request, 'mockform.html', context={**preValues, 'name_error': preValues['name'] == False, 'city_error': preValues['city'] == False, 'phone_error': preValues['phone'] == False, 'district_error': preValues['district'] == False})

        except Exception as e:
            preValues[audioField] = False
            # Error parsing text
            return render(request, 'mockform.html', context={**preValues, 'name_error': preValues['name'] == False, 'city_error': preValues['city'] == False, 'phone_error': preValues['phone'] == False, 'district_error': preValues['district'] == False})

    else:
        return render(request, 'mockform.html', context={'name': '',
            'city': '',
            'district': '',
            'phone': '',
        'name_error': True,'city_error': False,'district_error': False,'phone_error': False
        })



# # # myapp/views.py
# import os
# import speech_recognition as sr
# from gtts import gTTS
# from django.shortcuts import render
# from django.http import FileResponse
# from playsound import playsound

# def home(request):
#     return render(request, 'home.html')

# def ask_question(request):
#     if request.method == 'POST':
#         questions = ['તમારું નામ શું છે?', 'તમે ક્યાંથી છો?', 'તમારી ઉંમર કેટલી છે?']
#         answers = []

#         recognizer = sr.Recognizer()
#         microphone = sr.Microphone()

#         for question in questions:
#             while True:
#                 tts = gTTS(text=question, lang='gu')
#                 tts.save('question.mp3')
#                 playsound('question.mp3')

#                 with microphone as source:
#                     recognizer.adjust_for_ambient_noise(source)
#                     audio = recognizer.listen(source)

#                 try:
#                     answer = recognizer.recognize_google(audio, language='gu-IN')  # Set the language to Gujarati
#                     if answer:
#                         break  # loop tuti jase jo ene answer malse to
#                 except sr.UnknownValueError:
#                     answer = "Sorry, I didn't catch that."
#                 except sr.RequestError:
#                     answer = "Sorry, there was an issue with the speech recognition service."

#             answers.append(answer)

#         output_filename = os.path.join(os.path.dirname(__file__), 'output.txt')
#         with open(output_filename, 'w', encoding='utf-8') as f:  # Set encoding to 'utf-8' for Gujarati characters
#             for i in range(len(questions)):
#                 f.write(f"Question: {questions[i]}\n")
#                 f.write(f"Answer: {answers[i]}\n\n")

#         return render(request, 'answers.html', {'answers': answers,'questions': questions})

#     return render(request, 'question.html')

# def download_output(request):
#     output_filename = os.path.join(os.path.dirname(__file__), 'output.txt')
#     response = FileResponse(open(output_filename, 'rb'))
#     response['Content-Disposition'] = 'attachment; filename="output.txt"'
#     return response
