# Ollama Telegram Bot

A small Python script that queries an LLM via Ollama and sends the response to a Telegram bot.

Designed for automation.

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

# Automation with systemd

For scheduled execution on Linux systems, you can use the provided systemd service and timer files.

### Installation

1. Copy and customize the example files:
```bash
cp systemd/ollama_telegram_bot.service.example systemd/ollama_telegram_bot.service
cp systemd/ollama_telegram_bot.timer.example systemd/ollama_telegram_bot.timer
```

2. Edit both files and replace the placeholder paths:
   - `your_user_name` - your Linux username
   - `your_group` - your group (usually the same as username)
   - `/absolute/path/to/your/project` - full path to this repository
   - `/absolute/path/to/.venv` - full path to your Python virtual environment

3. Copy the files to systemd:
```bash
sudo cp systemd/ollama_telegram_bot.service /etc/systemd/system/
sudo cp systemd/ollama_telegram_bot.timer /etc/systemd/system/
```

4. Reload systemd and enable the timer:
```bash
sudo systemctl daemon-reload
sudo systemctl enable ollama_telegram_bot.timer
sudo systemctl start ollama_telegram_bot.timer
```

### Usage

Check timer status:
```bash
systemctl status ollama_telegram_bot.timer
```

View logs:
```bash
journalctl -u ollama_telegram_bot.service -f
```

Test the service manually:
```bash
sudo systemctl start ollama_telegram_bot.service
```

### Customizing the Schedule

The default timer runs every 2 hours between 08:00 and 00:00. To change this, edit the `OnCalendar` line in the timer file:
```ini
# Daily at 08:00
OnCalendar=*-*-* 08:00:00

# Every hour
OnCalendar=hourly

# Multiple times per day
OnCalendar=*-*-* 09:00,12:00,18:00:00
```

Test your calendar expression:
```bash
systemd-analyze calendar "*-*-* 08,10,12,14,16,18,20,22,00:00:00"
```

For more information on systemd timer syntax, see `man systemd.time`.