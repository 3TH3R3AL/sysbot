import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")

    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)

    # Capture the audio
    audio = r.listen(source)

try:
    # Use the Google Speech Recognition engine
    text = r.recognize_google(audio)

    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand.")
except sr.RequestError:
    print("Sorry, there was an issue with the service.")