from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Create a "route" that tells Flask what to do when someone visits the main page
@app.route('/')
def home():
    return "Hello! Jacobs Helper Bot is alive!"

# Run the server in debug mode
if __name__ == "__main__":
    app.run(debug=True)