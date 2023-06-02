import os
import subprocess

import speech_recognition as sr
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from gtts import gTTS
from speech_recognition import AudioFile, Recognizer, UnknownValueError

from .forms import AccountForm
from .models import Person

import os

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
