from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Paths to images
bot_image_path = "/static/assets/bot.png"
user_image_path = "/static/assets/user.png"

# Function to simulate loader effect
def loader(element):
    element = ""
    load_interval = 0
    while load_interval < 4:
        element += "."
        if element == "....":
            element = ""
        load_interval += 1

# Function to simulate typing effect
def type_text(element, text):
    for char in text:
        element += char

# Function to generate unique ID
def generate_unique_id():
    timestamp = str(time.time()).replace(".", "")
    random_number = str(random.random()).replace(".", "")
    return f"id-{timestamp}-{random_number}"

# Function to send prompt to language model
def get_bot_response(prompt):
    # Replace this URL with your language model server endpoint
    # model_endpoint = "http://localhost:5000"  # Example URL
    # response = requests.post(model_endpoint, json={"prompt": prompt})
    # if response.ok:
    #     return response.json().get("bot", "Error: No response from model")
    # else:
    return "Error: Failed to get response from model"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prompt", methods=["POST"])
def chat():
    prompt = request.json.get("prompt", "").strip()

    if prompt == "":
        return jsonify({"error": "Empty prompt"}), 400
    print(prompt)
    # User's chat stripe
    user_chat = {"isAi": False, "value": prompt}
    
    # Bot's chat stripe
    bot_chat = {"isAi": True, "value": get_bot_response(prompt)}
    print(user_chat,bot_chat)
    return jsonify({"user_chat": user_chat, "bot_chat": bot_chat})

if __name__ == "__main__":
    app.run(debug=True)