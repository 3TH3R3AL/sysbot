import speech_recognition
import pyttsx3
import subprocess


recognizer = speech_recognition.Recognizer()

def play_music():
    child_process = subprocess.Popen(['pithos'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, close_fds=True)
    # Detach the child process from the parent
    child_process.stdin.close()
    child_process.stdout.close()
    child_process.stderr.close()
    # Check if the child process is running
    if child_process.poll() is None:
        print("Child process is running independently.")


while True:
    try:
        with speech_recognition.Microphone() as mic:
            
            
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            print("Begin Speaking")
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Received command: {text}")
            if(text in ["system close","system closed","system clothes"]):
                break
            if(text in ["system play music","system crank them funky beats","system play them funky beats"]):
                play_music()
    except: 
        print("error")
        recognizer = speech_recognition.Recognizer()
        continue
