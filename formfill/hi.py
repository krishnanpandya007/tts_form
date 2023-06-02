import speech_recognition as sr
from gtts import gTTS

# Function to convert audio file to text
def extract_text_from_audio(audio_file):
    # Initialize the recognizer
    r = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        # Read the entire audio file
        audio = r.record(source)

        # Convert speech to text
        try:
            text = r.recognize_google(audio, language="gu-IN")  # Specify Gujarati language
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return None

# Path to the audio file
audio_file_path = "audio/recording_0.wav"

# Extract text from audio file
text = extract_text_from_audio(audio_file_path)

if text:
    print("Extracted Text:")
    print(text)

    # Convert text to speech
    tts = gTTS(text, lang="gu")  # Specify Gujarati language
    tts.save("output.mp3")
    print("Text converted to speech and saved as 'output.mp3'.")
else:
    print("No text extracted from the audio file.")
