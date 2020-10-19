#Online Synthesis
import gtts
from playsound import playsound

# make a request to google to get synthesis
tts = gtts.gTTS("The person in front of you is wearing a mask")

#save the audio file
tts.save("human_with_mask.mp3")

#play the audio file
playsound("human_with_mask.mp3")
