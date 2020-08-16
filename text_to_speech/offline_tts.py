# Offline Synthesis
import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()

# convert this text to speech
text = "It's a beautiful day today"

# get details of speaking rate
rate = engine.getProperty("rate")
print(rate)

# setting new voice rate (slower)
engine.setProperty("rate",100)

# for setting the voice raye (faster) just increase the rate 
#engine.setProperty("rate",300)

engine.say(text)

# play the peech
engine.runAndWait()
