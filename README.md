# AI_AGENT_RASPBERRY_PI


jarvis/
│
├── main.py                 # Main agent loop
├── config.py               # API keys/settings
│
├── utils/
│   ├── __init__.py
│   ├── audio_to_text.py    # Microphone → text
│   ├── text_to_audio.py    # Text → speaker
│   └── logger.py            # Logging
│
├── brain/
│   ├── __init__.py
│   └── llm.py              # LLM/API call
│
├── tools/
│   ├── __init__.py
│   ├── system_tools.py     # Open apps, shutdown, volume, etc.
│   ├── web_tools.py        # Search/web information
│   └── tool_manager.py     # Decide which tool to execute
│
├── memory/
│   ├── __init__.py
│   └── memory.py           # Conversation memory
│
└── requirements.txt