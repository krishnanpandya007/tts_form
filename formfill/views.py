import speech_recognition as sr
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def extract_text_from_audio(request):
    if request.method == 'POST' and request.FILES.get('audioFile'):
        audio_file = request.FILES['audioFile']

        # Configure the speech recognizer
        recognizer = sr.Recognizer()

        try:
            # Load the audio file
            with sr.AudioFile(audio_file) as source:
                audio = recognizer.record(source)

            # Extract text from audio
            text = recognizer.recognize_google(audio)

            # Return the extracted text as JSON response
            return JsonResponse({'text': text}, status=200)

        except sr.UnknownValueError:
            return JsonResponse({'error': 'Unable to transcribe audio. Speech not recognized.'}, status=400)

        except sr.RequestError:
            return JsonResponse({'error': 'Unable to transcribe audio. Recognition service error.'}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
