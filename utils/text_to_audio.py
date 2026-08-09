import pyttsx3


class TextToSpeech:

    def __init__(self):
        self.engine = pyttsx3.init()

        # Adjust speed if needed
        self.engine.setProperty("rate", 175)

        # Volume: 0.0 - 1.0
        self.engine.setProperty("volume", 1.0)

    def speak(self, text):

        self.engine.say(text)
        self.engine.runAndWait()