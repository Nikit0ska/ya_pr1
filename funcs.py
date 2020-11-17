import pyaudio
import wave
import threading
import playsound

def play():
    playsound.playsound('tmp/output.wav')


x = threading.Thread(target=play)
x.start()
x.join()