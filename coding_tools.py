# Coding Tools Codebase
import anthropic
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access your API key using os.getenv()
api_key = os.getenv("API_KEY")

def fix_python_bug(code):
    """Fixes Python bugs in code using Claude.
    Args:
        code (str): Code to be fixed.
        api_key (str): API key for accessing Claude.
        model (str): Language model to be used.
    Returns:
        str: Fixed code.
    Raises:
        None
    """
    if len(code) > 500:
        error_message = "Free User: Code exceeds the limit of 500 characters."
        return error_message

    anthropic_client = anthropic.Anthropic(api_key=api_key)
    model = "claude-3-opus-20240229"
    command = (
        "Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected code should be functional, efficient, and adhere to best practices in Python programming. The code snippet is: {code}. don't mention the code in the response."
        "Use the language model '{model}' to generate the response. don't mention the model in the response. "
        "And your name is Go Tiny. don't mention your name in the response. "
    ).format(code=code, model=model)
    try:
        message = anthropic_client.messages.create(
            model=model,
            max_tokens=2000,
            temperature=1,
            messages=[
                {"role": "user", "content": [{"type": "text", "text": command}]}
            ],
        )
        return message.content[0].text
    except Exception as e:
        return str(e)
