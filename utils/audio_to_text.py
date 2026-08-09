import speech_recognition as sr


class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        # How long silence is allowed before considering
        # the sentence finished.
        self.recognizer.pause_threshold = 2.0

        # Minimum audio before considering it speech.
        self.recognizer.phrase_threshold = 0.3

        # How much audio is kept before speech starts.
        self.recognizer.non_speaking_duration = 0.8

    def listen(self):

        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            # Do this once when the program starts ideally,
            # but keeping it here is okay for testing.
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            try:

                audio = self.recognizer.listen(
                    source,

                    # Maximum time waiting for you to START speaking
                    timeout=10,

                    # Maximum length of one command
                    # Increase this if you speak longer commands.
                    phrase_time_limit=30
                )

                print("🧠 Processing speech...")

                text = self.recognizer.recognize_google(
                    audio
                )

                print(f"👤 You: {text}")

                return text

            except sr.WaitTimeoutError:

                print("⏱️ No speech detected.")

                return ""

            except sr.UnknownValueError:

                print("❌ Could not understand audio.")

                return ""

            except sr.RequestError as e:

                print(f"❌ Speech recognition error: {e}")

                return ""