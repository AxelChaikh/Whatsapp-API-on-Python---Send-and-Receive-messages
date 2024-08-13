from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    entry = data.get('entry', [])[0]
    changes = entry.get('changes', [])[0]
    field = changes.get('field')

    if field == 'messages':
        # Manejar mensajes entrantes
        message_event = changes.get('value')
        print(f"Incoming message: {message_event}")
        # Aquí puedes agregar la lógica para manejar el mensaje entrante

    elif field == 'message_echoes':
        # Manejar mensajes salientes
        echo_event = changes.get('value')
        print(f"Outgoing message echo: {echo_event}")
        # Aquí puedes agregar la lógica para manejar el eco del mensaje saliente

    return jsonify(success=True)

@app.route('/webhook', methods=['GET'])
def verify():
    verify_token = "YOUR_VERIFY_TOKEN"
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if mode == 'subscribe' and token == verify_token:
        return challenge, 200
    else:
        return 'Verification failed', 403

if __name__ == '__main__':
    app.run(port=5000, debug=True)
