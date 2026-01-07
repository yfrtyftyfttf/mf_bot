from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # للسماح للموقع (Frontend) بمخاطبة السيرفر (Backend)

# بيانات البوت الخاصة بك
BOT_TOKEN = "7465926974:AAHzPv067I1ser4kExbRt5Hzj9R3Ma5Xjik"
CHAT_ID = "6695916631"

@app.route('/send_order', methods=['POST'])
def send_order():
    data = request.json
    order_type = data.get('type')
    details = data.get('details')

    # تنسيق الرسالة التي ستصلك في التلغرام
    message = f"🚨 {order_type} جديد:\n\n"
    for key, value in details.items():
        message += f"🔹 {key}: {value}\n"

    # إرسال الرسالة عبر API التلغرام
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return jsonify({"status": "success", "message": "تم الإرسال للبوت بنجاح"}), 200
    else:
        return jsonify({"status": "error", "message": "فشل في الإرسال"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
