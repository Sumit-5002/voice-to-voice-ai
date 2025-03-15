from flask import Flask, request, jsonify
from flask_cors import CORS
import cohere

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Replace with your Cohere API key
COHERE_API_KEY = "4wREYZeMqZlwG2G6AbNvwmzui9zn0aMo4NRtS3mf"
co = cohere.Client(COHERE_API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    """Receive user message and generate AI response"""
    try:
        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Generate response from Cohere
        response = co.generate(prompt=user_message)

        return jsonify({"response": response.generations[0].text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
