# Online Synthesis in spanish
# For more languages just see the lang.txt file

import gtts
from playsound import playsound

# make a request to google to get synthesis
tts = gtts.gTTS("Hola este soy yo", lang="es")

# save the audio file
tts.save("hola.mp3")

# play the audio file
playsound("hola.mp3")
