import os
from flask import Flask

app = Flask(__name__)

# Load keys from environment variables set on your server/hosting platform
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")
WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # --- 1. THE HANDSHAKE ---
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        return "Verification failed", 403

    # --- 2. THE PACKAGE OPENER ---
    elif request.method == 'POST':
        data = request.get_json()
        
        try:
            # Meta nests the actual message deep inside the payload
            entry = data.get('entry', [])[0]
            changes = entry.get('changes', [])[0]
            value = changes.get('value', {})
            
            # Check if this payload contains an actual user message
            if 'messages' in value:
                message = value['messages'][0]
                message_type = message.get('type')
                sender = message.get('from')
                
                print(f"\n📦 --- NEW MESSAGE FROM {sender} ---")
                
                # Extract basic Text
                if message_type == 'text':
                    text_body = message['text']['body']
                    print(f"Type: TEXT")
                    print(f"Content: {text_body}")
                
                # Extract a PDF / Document
                elif message_type == 'document':
                    media_id = message['document']['id']
                    file_name = message['document'].get('filename', 'Unknown_File')
                    print(f"Type: DOCUMENT / PDF")
                    print(f"Filename: {file_name}")
                    print(f"Media ID: {media_id}")
                    
                # Extract an Image
                elif message_type == 'image':
                    media_id = message['image']['id']
                    print(f"Type: IMAGE")
                    print(f"Media ID: {media_id}")
                    
                else:
                    print(f"Type: {message_type} (Unsupported in this version)")
                    
        except Exception as e:
            # Meta routinely sends status updates (like "Message Read" or "Delivered")
            # We can safely ignore those errors here.
            pass

        # We MUST return 200 OK, otherwise Meta assumes failure and retries for 7 days
        return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
