
from brain.llm_client import LLMClient
from utils.audio_to_text import SpeechToText
from utils.text_to_audio import TextToSpeech


class Jarvis:

    def __init__(self):

        self.llm = LLMClient()
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

        print("==========================")
        print("      JARVIS ONLINE")
        print("==========================")

    def process(self, user_input):

        # Send speech-to-text result to LLM
        response = self.llm.ask(user_input)

        # Show response in terminal
        print("\nJarvis:")
        print(response)

        # Speak response through headphones
        self.tts.speak(response)

    def run(self):

        while True:

            # Listen through microphone
            user_input = self.stt.listen()

            # Nothing understood
            if not user_input:
                continue

            # Show what the user said
            print(f"\nYou: {user_input}")

            # Exit commands
            if user_input.lower().strip() in [
                "exit",
                "quit",
                "goodbye",
                "stop"
            ]:
                print("Jarvis: Goodbye.")
                self.tts.speak("Goodbye.")
                break

            # Send speech to LLM
            self.process(user_input)


if __name__ == "__main__":

    jarvis = Jarvis()
    jarvis.run()

