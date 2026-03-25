from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from database import init_db

app = Flask(__name__, static_folder='public', static_url_path='')
CORS(app)

# Initialize Database on startup
init_db()

# Import Blueprints
from api.auth import auth_bp
from api.student import student_bp
from api.chatbot import chatbot_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(student_bp, url_prefix='/api/student')
app.register_blueprint(chatbot_bp, url_prefix='/api/chatbot')

# Serve Static files (Frontend)
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
