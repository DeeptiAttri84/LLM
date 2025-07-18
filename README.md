# 👩‍🍳 MomCares – Recipes & Chat ❤️

A friendly WhatsApp-style web application that provides AI-powered chat functionality and Indian-style recipe suggestions using LangChain and Ollama.

## Features

- **Interactive Chat**: Chat with an AI assistant in a WhatsApp-like interface
- **Recipe Generator**: Get Indian-style recipes based on available ingredients
- **Responsive Design**: Mobile-friendly interface with a modern UI
- **Session Management**: Maintains chat history during your session
- **Real-time Updates**: Instant responses with loading indicators

## Prerequisites

Before running the application, make sure you have the following installed:

- **Python 3.8+**
- **Ollama** (with a language model installed)
- **Git** (for cloning the repository)

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd momcares
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Setup Ollama

1. **Install Ollama**: Visit [ollama.ai](https://ollama.ai) and download Ollama for your operating system.

2. **Install a Language Model**: After installing Ollama, download a model (the app uses Mistral by default):
   ```bash
   ollama pull mistral
   ```

3. **Start Ollama Service**: Make sure Ollama is running:
   ```bash
   ollama serve
   ```

## Configuration

### Update Secret Key

Before running the application, update the Flask secret key in `app.py`:

```python
app.secret_key = 'your-secure-secret-key-here'  # Replace with a secure random string
```

### Change the Model (Optional)

If you want to use a different Ollama model, update the model name in `app.py`:

```python
llm = Ollama(model="your-preferred-model")  # e.g., "llama2", "codellama", etc.
```

## Project Structure

```
momcares/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Frontend template (embedded in app.py)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Running the Application

1. **Make sure Ollama is running**:
   ```bash
   ollama serve
   ```

2. **Start the Flask application**:
   ```bash
   python app.py
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

### Chat Tab 

1. Click on the "Chat" tab
2. Type your message in the input field
3. Press Enter or click "Send"
4. The AI assistant will respond in a friendly, WhatsApp-style format
5. Use "Clear Chat" to start a new conversation

### Recipe Tab 

1. Click on the "Get Recipe" tab
2. Enter the ingredients you have available (e.g., "potato, onion, tomato")
3. Click "Get Recipe"
4. The AI will suggest an Indian-style recipe using your ingredients

## API Endpoints

- `GET /` - Main application page
- `POST /send_message` - Send a chat message
- `POST /get_recipe` - Get a recipe based on ingredients
- `POST /clear_chat` - Clear chat history
- `GET /get_chat_history` - Retrieve chat history

## Customization

### Modify System Prompts

You can customize the AI's behavior by editing the system prompts in `app.py`:

```python
chat_system_prompt = """
Your custom chat instructions here...
"""

recipe_prompt = """
Your custom recipe instructions here...
"""
```

### Styling

The application uses embedded CSS. You can modify the styling by editing the `<style>` section in the HTML template or extract it to a separate CSS file.

## Troubleshooting

### Common Issues

1. **Ollama not found**: Make sure Ollama is installed and running
2. **Model not available**: Ensure you've pulled the model with `ollama pull mistral`
3. **Port already in use**: Change the port in `app.py`: `app.run(debug=True, port=5001)`
4. **Session issues**: Clear your browser cache and cookies

### Error Messages

- **"Please type something to send!"**: Enter a message before sending
- **"Please enter some ingredients!"**: Add ingredients before generating a recipe
- **"Something went wrong"**: Check if Ollama is running and the model is available

## Dependencies

```txt
flask
langchain-community
langchain
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request


## Screenshots

<p align="center">
  <img width="300" alt="Chat Suggestion" src="https://github.com/user-attachments/assets/88d2d700-09af-44f9-8c94-a210d9829ff3" />
  <img width="300" alt="Recipe Output" src="https://github.com/user-attachments/assets/e943dee6-d1d7-4692-9f5d-9d9c9aa0fff7" />
</p>
<p align="center"><em>Left: Chat interface showing a dinner suggestion request | Right: Recipe suggestions based on available ingredients</em></p>
