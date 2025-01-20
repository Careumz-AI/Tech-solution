from flask import Flask, request, jsonify
import grpc
import riva.client
from riva.client import ASRService, NLPService, Auth

app = Flask(_name_)

# Configure NVIDIA Riva server details
RIVA_SERVER = "localhost:50051"  # Update with actual Riva server address
auth = Auth(uri=RIVA_SERVER)
asr_service = ASRService(auth)
nlp_service = NLPService(auth)

@app.route("/speech-to-text", methods=["POST"])
def speech_to_text():
    """Handles speech-to-text conversion using NVIDIA Riva."""
    audio_data = request.files.get("audio")
    if not audio_data:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_bytes = audio_data.read()
    transcript = asr_service.offline_recognize(audio_bytes, "en-US")
    return jsonify({"transcript": transcript})

@app.route("/text-to-intent", methods=["POST"])
def text_to_intent():
    """Extracts intent from text input using Riva NLP."""
    data = request.json
    user_text = data.get("text", "")
    if not user_text:
        return jsonify({"error": "No text provided"}), 400
    
    response = nlp_service.classify_text([user_text])
    return jsonify({"intent": response})

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint to ensure the server is running."""
    return jsonify({"status": "Riva AI Virtual Health Assistant is running"})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)