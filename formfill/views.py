import speech_recognition as sr
from django.http import JsonResponse
from django.shortcuts import render
from .models import Person
from .forms import AccountForm

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


def submit_form_api(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']
            mobile_number = form.cleaned_data['mobile_number']
            
            user = Person(name=name, city=city, district=district, mobile_number=mobile_number)
            user.save()

            return JsonResponse({'success': True, 'message': 'Form submitted successfully'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)