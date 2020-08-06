#Online Synthesis
import gtts
from playsound import playsound

# make a request to google to get synthesis
tts = gtts.gTTS("Hi, This is Ashwini Jha")

#save the audio file
tts.save("hi.mp3")

#play the audio file
playsound("hi.mp3")
