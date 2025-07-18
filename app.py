from flask import Flask, render_template, request, jsonify, session
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Initialize model
llm = Ollama(model="mistral")  # Use your preferred model

# System prompts
chat_system_prompt = """
You are a friendly assistant chatting on WhatsApp.
Talk casually with the user. Use short messages, line breaks, and emojis.
"""

recipe_prompt = """
You are a friendly cooking assistant on WhatsApp.
The user will give you ingredients.
Reply with a simple Indian-style recipe using those ingredients.
Use short sentences, line breaks, and emojis.
"""

def chat_with_user(history):
    # Create prompt with entire history
    messages = [("system", chat_system_prompt)]
    for msg in history:
        messages.append(("user", msg["user"]))
        messages.append(("assistant", msg["bot"]))
    
    prompt_template = ChatPromptTemplate.from_messages(messages)
    prompt = prompt_template.format_messages()
    return llm.invoke(prompt)

def get_recipe(user_ingredients):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", recipe_prompt),
        ("user", f"I have these ingredients: {user_ingredients}. Suggest a recipe!")
    ])
    prompt = prompt_template.format_messages()
    return llm.invoke(prompt)

@app.route('/')
def index():
    # Initialize session if not exists
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_input = request.json.get('message', '').strip()
        
        if not user_input:
            return jsonify({'error': 'Please type something to send!'}), 400
        
        # Initialize chat history if not exists
        if 'chat_history' not in session:
            session['chat_history'] = []
        
        # Get bot response
        chat_history = session['chat_history']
        
        # Add user message temporarily to get context
        temp_history = chat_history + [{"user": user_input, "bot": ""}]
        
        # Get response from bot
        response = chat_with_user(temp_history)
        
        # Add the conversation to history
        session['chat_history'].append({"user": user_input, "bot": str(response)})
        session.modified = True
        
        return jsonify({
            'user_message': user_input,
            'bot_response': str(response)
        })
    
    except Exception as e:
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500

@app.route('/get_recipe', methods=['POST'])
def get_recipe_route():
    try:
        ingredients = request.json.get('ingredients', '').strip()
        
        if not ingredients:
            return jsonify({'error': 'Please enter some ingredients!'}), 400
        
        recipe = get_recipe(ingredients)
        return jsonify({'recipe': str(recipe)})
    
    except Exception as e:
        return jsonify({'error': f'Failed to generate recipe: {str(e)}'}), 500

@app.route('/clear_chat', methods=['POST'])
def clear_chat():
    session['chat_history'] = []
    session.modified = True
    return jsonify({'success': True})

@app.route('/get_chat_history')
def get_chat_history():
    return jsonify(session.get('chat_history', []))

if __name__ == '__main__':
    app.run(debug=True)