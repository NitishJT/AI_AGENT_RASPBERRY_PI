# 🤖 JARVIS — AI Voice Agent

A personal **AI voice assistant** being developed with Python, designed to eventually run on a **Raspberry Pi**.

The current version runs locally on a PC and uses a remotely hosted **Qwen 2.5 1.5B** model as the AI brain. Voice input is converted to text, sent to the LLM through a FastAPI endpoint, and the response is both displayed in the terminal and spoken through the connected headset.

The long-term goal is to turn this into a modular **Jarvis-style AI agent** capable of interacting with the computer, controlling hardware, using tools, maintaining memory, and eventually running on a Raspberry Pi.

---

## 🧠 Current Architecture

```text
                    ┌──────────────────────────┐
                    │       USER               │
                    │                          │
                    │   🎤 Speaks to Jarvis    │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │   Speech-to-Text (STT)   │
                    │                          │
                    │   audio_to_text.py       │
                    └────────────┬─────────────┘
                                 │
                                 │ Text
                                 ▼
                    ┌──────────────────────────┐
                    │        main.py           │
                    │                          │
                    │   Jarvis Agent Controller│
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │     llm_client.py        │
                    │                          │
                    │    HTTPS API Request     │
                    └────────────┬─────────────┘
                                 │
                                 │ HTTPS
                                 ▼
              ┌─────────────────────────────────────┐
              │          HUGGING FACE               │
              │                                     │
              │          FastAPI Server             │
              │                                     │
              │       POST /generate                │
              │              │                      │
              │              ▼                      │
              │       Qwen 2.5 1.5B GGUF            │
              │                                     │
              └──────────────┬──────────────────────┘
                             │
                             │ Response
                             ▼
                    ┌──────────────────────────┐
                    │        main.py           │
                    └────────────┬─────────────┘
                                 │
                       ┌─────────┴─────────┐
                       │                   │
                       ▼                   ▼
              ┌────────────────┐   ┌────────────────┐
              │    Terminal    │   │ Text-to-Speech │
              │                │   │                │
              │  Print answer  │   │ pyttsx3        │
              └────────────────┘   └───────┬────────┘
                                           │
                                           ▼
                                      🎧 Headset
```

---

# ✨ Current Features

### 🎤 Voice Input

Jarvis can listen to commands through the computer's microphone/headset.

Speech is converted into text using the Speech Recognition module.

Example:

```text
User:
"Jarvis, what is Python?"
```

becomes:

```text
"What is Python?"
```

---

### 🧠 AI Brain

The AI model is **Qwen 2.5 1.5B Instruct**, running remotely through a Hugging Face deployment.

The Raspberry Pi/PC does **not** need to load the LLM locally.

Current API:

```text
POST /generate
```

Hugging Face endpoint:

```text
https://{USERNAME}.hf.space/generate
```

The client sends a request similar to:

```json
{
  "prompt": "What is Python?",
  "max_tokens": 300,
  "temperature": 0.4,
  "top_p": 0.9
}
```

The API returns:

```json
{
  "output": "Python is a high-level programming language..."
}
```

---

### 🔊 Text-to-Speech

The LLM response is:

1. Printed in the terminal.
2. Converted to speech.
3. Played through the connected headphones/speaker.

Example:

```text
You:
What is Python?

JARVIS:
Python is a high-level programming language...
```

The same response is spoken through the headset.

---

### 🆔 JARVIS Identity

The assistant is configured with a system context identifying it as:

```text
JARVIS
```

The model is instructed to identify itself as JARVIS rather than Qwen or another AI assistant.

---

# 📁 Project Structure

Current project structure:

```text
AI_AGENT_RASPBERRY_PI/
│
├── main.py
├── config.py
│
├── brain/
│   ├── __init__.py
│   └── llm_client.py
│
├── utils/
│   ├── __init__.py
│   ├── audio_to_text.py
│   └── text_to_audio.py
│
├── tools/
│   ├── __init__.py
│   └── ...
│
├── memory/
│   ├── __init__.py
│   └── ...
│
└── README.md
```

---

# 📄 File Responsibilities

## `main.py`

The main controller of the Jarvis application.

Responsible for coordinating:

```text
Speech
   ↓
LLM
   ↓
Response
   ↓
Terminal + Voice
```

It initializes the major components and keeps the assistant running in a loop.

---

## `config.py`

Contains application configuration such as:

* Hugging Face API endpoint
* Assistant name
* System prompt
* LLM parameters

Example:

```python
ASSISTANT_NAME = "JARVIS"
```

Keeping configuration separate makes it easier to change settings without modifying the core agent logic.

---

## `brain/llm_client.py`

Responsible for communicating with the remote Qwen model.

It sends HTTP requests to:

```text
https://{USERNAME}.hf.space/generate
```

and extracts the generated response.

The Raspberry Pi does not need:

```text
llama-cpp-python
```

or the GGUF model itself.

---

## `utils/audio_to_text.py`

Handles microphone input and converts speech into text.

Current development target:

```text
🎤 Microphone
      ↓
Speech Recognition
      ↓
Text
```

The implementation can later be replaced with a more advanced STT system such as Whisper without changing the rest of the agent architecture.

---

## `utils/text_to_audio.py`

Handles text-to-speech.

Current implementation uses:

```text
pyttsx3
```

Flow:

```text
LLM response
     ↓
pyttsx3
     ↓
🎧 Headphones
```

---

## `tools/`

This directory will contain the actions that Jarvis can perform.

Planned tools include:

```text
System Tools
├── Open applications
├── Get CPU usage
├── Get RAM usage
├── Get system information
├── Shutdown
└── Restart

Web Tools
├── Web search
├── Weather
└── News

Hardware Tools
├── GPIO
├── LED
├── Sensors
├── Servo
└── OLED

Vision Tools
└── Camera / Image detection
```

Tool execution will eventually be controlled by the agent rather than allowing the LLM to directly execute arbitrary code.

---

# 🧠 Planned Agent Architecture

The current system is intentionally simple.

The next stage is to turn it into a proper tool-using agent:

```text
User
 ↓
Speech-to-Text
 ↓
JARVIS Agent
 ↓
Qwen
 ↓
Decision
 ├── Normal response
 │       ↓
 │      TTS
 │
 └── Tool required
         ↓
    Tool Manager
         ↓
    Execute Tool
         ↓
      Result
         ↓
       Qwen
         ↓
     Final Answer
         ↓
        TTS
```

For example:

```text
User:
"Jarvis, open Chrome."
```

The model could determine:

```text
TOOL: open_browser
```

Then:

```text
main.py
   ↓
tool_manager.py
   ↓
system_tools.py
   ↓
Chrome
```

Jarvis would then respond:

```text
"Chrome is open."
```

---

# 🧩 Planned Components

The following components are planned for future versions.

### 🔧 Tool System

A centralized tool manager will allow Jarvis to use predefined capabilities safely.

Potential tools:

* Application launcher
* File operations
* Calculator
* System monitoring
* Web search
* Weather
* GPIO control
* Camera
* OLED display

---

### 🧠 Memory

A lightweight memory system will allow Jarvis to retain useful information between conversations.

Initial implementation may use a simple local file/database.

Future options may include:

```text
SQLite
JSON
Vector Database
```

The memory system will be designed with the Raspberry Pi's limited resources in mind.

---

### 👁️ Computer Vision

A future version may connect an ESP32-CAM or Raspberry Pi camera.

Potential capabilities:

```text
Camera
   ↓
Image
   ↓
Computer Vision
   ↓
Jarvis
```

Possible applications:

* Object detection
* Face detection
* Environment awareness
* Image analysis

---

### 📺 OLED Display

The Raspberry Pi version will eventually use an OLED display for visual feedback.

Possible states:

```text
JARVIS ONLINE

LISTENING...

THINKING...

EXECUTING...

SPEAKING...
```

---

# 🍓 Raspberry Pi Deployment

The final target hardware is a **Raspberry Pi 3 Model A+**.

The Pi will act as the physical interface for Jarvis.

```text
Raspberry Pi
│
├── 🎤 Microphone
├── 🔊 Speaker / Headphones
├── 📺 OLED
├── 📷 Camera
├── ⚡ GPIO
└── 🌐 Internet
        │
        ▼
   Hugging Face
        │
        ▼
   Qwen 2.5 1.5B
```

The Qwen model will remain hosted remotely because running a modern LLM locally on the Raspberry Pi 3 A+ is not practical for this project.

---

# 🚀 Running the Current Version

## 1. Clone the repository

```bash
git clone https://github.com/NitishJT/AI_AGENT_RASPBERRY_PI.git
cd AI_AGENT_RASPBERRY_PI
```

## 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux / Raspberry Pi:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

For the current PC voice test, the main dependencies include:

```text
requests
SpeechRecognition
PyAudio
pyttsx3
```

---

## 4. Configure the LLM endpoint

The current Qwen API endpoint is configured in:

```text
config.py
```

Current endpoint:

```text
https://{USERNAME}.hf.space/generate
```

---

## 5. Start Jarvis

```bash
python main.py
```

Jarvis should start listening through the configured microphone.

Example:

```text
==========================
      JARVIS ONLINE
==========================

🎤 Listening...
```

Speak a command.

The recognized text will appear in the terminal, followed by the Qwen response.

The response will also be spoken through the configured audio output.

---

# 🔐 Security

The project is currently under active development.

Do **not** commit:

```text
API keys
Access tokens
Passwords
Private credentials
Personal data
```

If authentication is added to the Hugging Face endpoint, credentials should be stored using environment variables rather than directly inside the source code.

Example:

```python
import os

HF_API_KEY = os.getenv("HF_API_KEY")
```

---

# 🛠️ Development Roadmap

## Phase 1 — PC Prototype

* [x] Python project structure
* [x] Hugging Face Qwen endpoint
* [x] LLM client
* [x] Text interaction
* [x] Speech-to-text
* [x] Text-to-speech
* [x] Terminal response
* [x] Voice response
* [x] JARVIS identity

## Phase 2 — Agent

* [ ] Tool manager
* [ ] System tools
* [ ] Application launcher
* [ ] Calculator
* [ ] System monitoring
* [ ] Tool-use loop
* [ ] Conversation context
* [ ] Better prompt management

## Phase 3 — Memory

* [ ] Short-term conversation memory
* [ ] Persistent memory
* [ ] User preferences
* [ ] Context retrieval

## Phase 4 — Raspberry Pi

* [ ] Raspberry Pi setup
* [ ] USB microphone
* [ ] Audio output
* [ ] OLED display
* [ ] GPIO tools
* [ ] Automatic startup
* [ ] Background service

## Phase 5 — Vision

* [ ] Raspberry Pi camera
* [ ] ESP32-CAM integration
* [ ] Object detection
* [ ] Image understanding

## Phase 6 — Advanced JARVIS

* [ ] Wake-word detection
* [ ] Multi-tool planning
* [ ] Web search
* [ ] Hardware control
* [ ] Context-aware responses
* [ ] Autonomous task execution
* [ ] Better conversational memory

---

# 🎯 Final Goal

The goal of this project is to create a modular personal AI assistant inspired by **JARVIS**.

The final system should be able to:

```text
Listen
   ↓
Understand
   ↓
Think
   ↓
Use Tools
   ↓
Interact with Hardware
   ↓
Remember
   ↓
Respond
```

while keeping the Raspberry Pi lightweight by using a remotely hosted LLM as its primary AI brain.

---

## Project Status

🚧 **Currently in active development**

**Current milestone:**

> PC-based voice assistant → Hugging Face Qwen → Terminal + Voice Response

**Next milestone:**

> Tool-using AI agent with system controls and memory
