# app/routes.py

from flask import Blueprint, render_template, request, jsonify
import re
from .utils import format_response
from .chat import ChatManager

main = Blueprint('main', __name__)

chat_manager = ChatManager()  

@main.route('/')
def index():
    """Render the chat interface."""
    return render_template('chat.html')  


@main.route('/api/chat', methods=['POST'])
def chat():
    
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    
    ai_response = chat_manager.get_response(user_message)

    formatted_response = format_response(ai_response)

    return jsonify({"response": formatted_response})  
