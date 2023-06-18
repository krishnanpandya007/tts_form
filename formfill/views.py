import os
import subprocess

import speech_recognition as sr
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from gtts import gTTS
from speech_recognition import AudioFile, Recognizer, UnknownValueError

from .forms import AccountForm, UploadAudioFileForm
from .models import Person, AudioRecord

import os

def home(request):
    return render(request, 'home.html')
def home2(request):
    return render(request, 'home2.html')

def index(request):
    audio_dir = '/home/aluminium/Documents/tts_final/tts_form/audio'

    # Create the 'audio' directory if it doesn't exist
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)

    count = len(os.listdir(audio_dir))
    filename = f'recording_{count}.wav'

    if request.method == 'POST':
        audio_file = request.FILES['audio']

        audio_path = os.path.join(audio_dir, filename)
        with open(audio_path, 'wb') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)

    return render(request, 'index.html')

# import speech_recognition as sr
# from gtts import gTTS

# # Function to convert audio file to text
# def extract_text_from_audio(audio_file):
#     # Initialize the recognizer
#     r = sr.Recognizer()

#     # Load the audio file
#     with sr.AudioFile(audio_file) as source:
#         # Read the entire audio file
#         audio = r.record(source)

#         # Convert speech to text
#         try:
#             text = r.recognize_google(audio, language="gu-IN")  # Specify Gujarati language
#             return text
#         except sr.UnknownValueError:
#             print("Google Speech Recognition could not understand audio.")
#         except sr.RequestError as e:
#             print("Could not request results from Google Speech Recognition service; {0}".format(e))

#     return None

# # Path to the audio file
# audio_file_path = "/home/aluminium/Downloads/recording_0(1).wav"

# # Extract text from audio file
# text = extract_text_from_audio(audio_file_path)

# if text:
#     print("Extracted Text:")
#     print(text)

#     # Convert text to speech
#     tts = gTTS(text, lang="gu")  # Specify Gujarati language
#     tts.save("output.mp3")
#     print("Text converted to speech and saved as 'output.mp3'.")
# else:
#     print("No text extracted from the audio file.")



















def mockform(request):
    if request.method == 'POST':
        prevErrors = request.POST.get('currErrors', '').split(',')
        preValues = {
            'name': False if prevErrors[0]=='True' else request.POST.get('label-name', ''),
            'district': False if prevErrors[1]=='True' else request.POST.get('label-district', ''),
            'city': False if prevErrors[2]=='True' else request.POST.get('label-city', ''),
            'phone': False if prevErrors[3]=='True' else request.POST.get('label-phone', ''),
        }
        print(preValues)
        labels = ['name', 'district', 'city', 'phone', 'submit']

        direction = request.POST['direction'] # prev | next
        if(request.POST['currentField'] == 'submit' and direction == 'next'):
            # Time to submit form
            if(any([v== False for k, v in preValues.items()])):
                # Time to abort
                return render(request, 'mockform.html', context={**preValues, 'name_error': preValues['name'] == False, 'city_error': preValues['city'] == False, 'phone_error': preValues['phone'] == False, 'district_error': preValues['district'] == False, 'targetField': labels[prevIndex]})
            else:
                # No Errors, we can save the form
                Person.objects.create(name=preValues['name'], district=preValues['district'], city=preValues['city'], mobile_number=preValues['phone'])
                return render(request, 'success.html')
        nextIndex = labels.index(request.POST['currentField']) + 1
        prevIndex = max(labels.index(request.POST['currentField']) - 1, 0)
        name_audio_file = request.FILES.get(f"{request.POST['currentField']}_audio")

        if(not name_audio_file):
            # Mock Navigation with context data currentField
            if(direction == 'next'):
                return render(request, 'mockform.html', context={**preValues, 'name_error': preValues['name'] == False, 'city_error': preValues['city'] == False, 'phone_error': preValues['phone'] == False, 'district_error': preValues['district'] == False, 'targetField': labels[nextIndex]})
            else:
                return render(request, 'mockform.html', context={**preValues, 'name_error': preValues['name'] == False, 'city_error': preValues['city'] == False, 'phone_error': preValues['phone'] == False, 'district_error': preValues['district'] == False, 'targetField': labels[prevIndex]})

        # form = UploadAudioFileForm(request.POST, request.FILES)
        # file_instance:AudioRecord
        # if form.is_valid():
        #     title = form.cleaned_data['label']
        file_instance = AudioRecord(label=request.POST['currentField'], audio_file=request.FILES[f"{request.POST['currentField']}_audio"])
        file_instance.save()
        # else:
        #     print("ERR")
        path = file_instance.audio_file.path
        print("APTH::", path)
        # print(type(request.POST['name_audio']))
        # audio_file = request.FILES['audioFile']
        # audioField = request.GET.get('audioField', '') # name | city | district | phone
        # preName = request.GET.get('name', '')
        # preCity = request.GET.get('city', '')
        # preDistrict = request.GET.get('district', '') 
        # prePhone = request.GET.get('phone', '') 

        # Configure the speech recognizer
        recognizer = sr.Recognizer()

        try:
            # Load the audio file
            with sr.AudioFile(file_instance.audio_file) as source:
                audio = recognizer.record(source)

            # Extract text from audio
            text = recognizer.recognize_google(audio, language='gu-IN')
            if(request.POST['currentField'] == 'phone'):
                # No need of spaces in phone number
                text = text.replace(' ', '')
            print("Extracted::", text)

            preValues[request.POST['currentField']] = text # currentField
            if(direction == 'next'):
                return render(request, 'mockform.html', context={**preValues, 'name_error': preValues['name'] == False, 'city_error': preValues['city'] == False, 'phone_error': preValues['phone'] == False, 'district_error': preValues['district'] == False, 'targetField': labels[nextIndex]})
            else:
                return render(request, 'mockform.html', context={**preValues, 'name_error': preValues['name'] == False, 'city_error': preValues['city'] == False, 'phone_error': preValues['phone'] == False, 'district_error': preValues['district'] == False, 'targetField': labels[prevIndex]})

        except Exception as e:
            preValues[request.POST['currentField']] = False
            # Error parsing text
            return render(request, 'mockform.html', context={**preValues, 'name_error': preValues['name'] == False, 'city_error': preValues['city'] == False, 'phone_error': preValues['phone'] == False, 'district_error': preValues['district'] == False, 'targetField': request.POST['currentField']})

    else:
        return render(request, 'mockform.html', context={'name': '',
            'city': '',
            'district': '',
            'phone': '',
        'name_error': False,'city_error': False,'district_error': False,'phone_error': False, 'targetField': 'name'
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
