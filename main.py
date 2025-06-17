from flask import Flask, request
import requests

app = Flask(__name__)

# Replace with your actual Telegram Bot Token and Chat ID
BOT_TOKEN = "8153432908:AAEaq614eR8-Fz6g_6vr3XbcmHMwko3E3Jc"
CHAT_ID = "7910438097"

@app.route('/rsialert', methods=['GET', 'POST'])
def rsialert():
    # Get message from query parameter (GET) or POST data
    message = request.args.get('message') or request.form.get('message')

    if message:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message
        }
        response = requests.post(url, data=payload)
        return f"Alert sent: {message}"
    
    return "RSI alert webhook is live"
