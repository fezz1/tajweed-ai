import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Tajweed educational data
TAJWEED_RULES = {
    "izhar": "Izhar means 'to make clear'. Pronounce the Noon Sakinah or Tanween clearly without extra nasalization (Ghunnah) when followed by throat letters: ء, ه, ع, ح, غ, خ.",
    "idgham": "Idgham means 'to merge'. Merge the Noon Sakinah or Tanween into the next letter with Ghunnah for (ي, ن, م, و) and without Ghunnah for (ل, ر).",
    "iqlab": "Iqlab means 'to convert'. Change the Noon Sakinah or Tanween into a hidden Meem sound with Ghunnah when followed by the letter ب.",
    "ikhfa": "Ikhfa means 'to hide'. Conceal the Noon Sakinah or Tanween sound with a light Ghunnah before the remaining 15 letters of the alphabet."
}

@app.route("/", methods=["GET"])
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Interactive Tajweed AI Companion</title>
        <style>
            body { font-family: 'Segoe UI', Arial, sans-serif; background: #f0f4f8; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .chat-container { width: 450px; height: 550px; background: white; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.15); display: flex; flex-direction: column; overflow: hidden; }
            .header { background: #1b4d3e; color: white; padding: 15px; text-align: center; font-size: 1.2em; font-weight: bold; }
            .chat-box { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; background: #fafbfc; }
            .msg { padding: 10px 14px; border-radius: 8px; max-width: 80%; line-height: 1.4; font-size: 0.95em; }
            .user { background: #1b4d3e; color: white; align-self: flex-end; }
            .bot { background: #eaeff2; color: #2d3748; align-self: flex-start; }
            .input-area { display: flex; padding: 12px; background: white; border-top: 1px solid #e2e8f0; }
            input { flex: 1; padding: 12px; border: 1px solid #cbd5e1; border-radius: 6px; outline: none; font-size: 1em; }
            button { background: #1b4d3e; color: white; border: none; padding: 0 18px; margin-left: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="chat-container">
            <div class="header">🌙 Tajweed Learning Assistant</div>
            <div class="chat-box" id="chatBox">
                <div class="msg bot">Assalamu Alaikum! Ask me about Tajweed rules. Try typing: <b>Izhar</b>, <b>Idgham</b>, <b>Iqlab</b>, or <b>Ikhfa</b>.</div>
            </div>
            <div class="input-area">
                <input type="text" id="userInput" placeholder="Ask a Tajweed question..." onkeypress="handleKey(event)">
                <button onclick="sendMessage()">Ask</button>
            </div>
        </div>
        <script>
            async function sendMessage() {
                const input = document.getElementById('userInput');
                const text = input.value.trim();
                if (!text) return;
                appendMessage(text, 'user');
                input.value = '';

                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
                const data = await response.json();
                appendMessage(data.reply, 'bot');
            }
            function appendMessage(text, sender) {
                const chatBox = document.getElementById('chatBox');
                const msgDiv = document.createElement('div');
                msgDiv.className = `msg ${sender}`;
                msgDiv.innerHTML = text;
                chatBox.appendChild(msgDiv);
                chatBox.scrollTop = chatBox.scrollHeight;
            }
            function handleKey(e) { if (e.key === 'Enter') sendMessage(); }
        </script>
    </body>
    </html>
    """

@app.route("/chat", methods=["POST"])
def chat():
    user_data = request.get_json() or {}
    msg = user_data.get("message", "").lower()
    
    # Matching rule keys
    reply = "I can help you learn Tajweed! Try asking specifically about rules like <b>Izhar</b>, <b>Idgham</b>, <b>Iqlab</b>, or <b>Ikhfa</b>."
    for rule, description in TAJWEED_RULES.items():
        if rule in msg:
            reply = description
            break
            
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
