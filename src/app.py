from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes and origins


@app.route("/")
def hello_world():
  return {"message": "Hello, World!"}  # Returning JSON is common for CORS APIs

@app.get("/hello")
def hello_wwworld():
  return {"message": "Helldasdsadsao, World!"}  # Returning JSON is common for CORS APIs


if __name__ == "__main__":
  # host="0.0.0.0" makes the server accessible from other devices on your network
  app.run(host="0.0.0.0", port=5000 )