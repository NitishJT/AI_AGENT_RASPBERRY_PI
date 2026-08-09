import json
import os


MEMORY_FILE = "memory.json"


class Memory:

    def __init__(self):

        self.memory = self.load()

    def load(self):

        if not os.path.exists(MEMORY_FILE):
            return []

        try:

            with open(
                MEMORY_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except Exception:

            return []

    def add(self, role, content):

        self.memory.append({
            "role": role,
            "content": content
        })

        self.save()

    def save(self):

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.memory,
                file,
                indent=2
            )

    def get_recent(self, count=10):

        return self.memory[-count:]