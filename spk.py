import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
class fx:

    def speakf(self,audio,rateofthesound):
        v = rateofthesound
        engine.setProperty("rate",v)
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()
    def speakm(self,audio):
        engine.setProperty("rate",180)
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()
# b = fx()
# b.speakf('vbdhfvbhdf',50)



