# Ollama Telegram Bot

A small Python script that queries an LLM via Ollama and sends the response to a Telegram bot.

Designed for cron-based automation.

Typical use cases:
- motivational messages
- daily summaries
- reminders
- random thoughts


## Configuration

Create a `.env` file with the following variables:

```env
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=llama3.2:1b
OLLAMA_PROMPT=Send a short, motivating message.
TELEGRAM_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```