import requests
from dotenv import load_dotenv
import os
load_dotenv()
USERNAME = os.getenv("HUGGING_FACE")

class LLMClient:

    def __init__(self):
        self.endpoint = (
            f"https://{USERNAME}.hf.space/generate"
        )

    def ask(
        self,
        prompt,
        max_tokens=300,
        temperature=0.4,
        top_p=0.9
    ):

        payload = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p
        }

        try:

            response = requests.post(
                self.endpoint,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            return data["output"]

        except requests.exceptions.Timeout:

            return "The AI server took too long to respond."

        except requests.exceptions.RequestException as e:

            print("LLM API error:", e)

            return "I could not connect to my AI brain."