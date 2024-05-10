# AI Tools Codebase
import anthropic
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access your API key using os.getenv()
api_key = os.getenv("API_KEY")
def shorten_content(content):
    """Shortens content using Claude.
    Args:
        content (str): Content to be shortened.
        api_key (str): API key for accessing Claude.
        model (str): Language model to be used.
    Returns:
        str: Shortened content.
    Raises:
        None
    """
    if len(content) > 500:
        error_message = "Free User can't shorten more than 500 words. Please use other tools."
        return error_message

    anthropic_client = anthropic.Anthropic(api_key=api_key)
    model = "claude-3-opus-20240229"
    command = (
        "Please shorten the following content: {content}. don't mention the content in the response."
        "Only return the shortened content, without any additional text or explanations. "
        "Use the language model '{model}' to generate the response. don't mention the model in the response. "
        "And your name is Go Tiny. don't mention your name in the response. "
    ).format(content=content, model=model)

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
