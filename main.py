from flask import Flask, request
import requests, os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv('TELE_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELE_CHAT_ID')

@app.route('/', methods=['GET'])
def home():
    return "✅ RSI Alert Webhook is live"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json or {}
    condition = data.get('condition', 'No Condition')
    rsi = data.get('rsi', 'N/A')
    message = f"📢 RSI Alert:\nCondition: {condition}\nRSI: {rsi}"

    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        data={'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    )
    return '✅ Alert sent to Telegram', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)