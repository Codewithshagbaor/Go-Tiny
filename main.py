from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import logging
from tools.ai_tools import shorten_content
from tools.coding_tools import fix_python_bug
from tools.password_tool import generate_password
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access your API key using os.getenv()
Token = os.getenv("TOKEN")
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Define command handlers for your bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🗂️ Categories", callback_data="categories"),
            InlineKeyboardButton("🛠️ Tools", callback_data="tools")
        ],
        [
            InlineKeyboardButton("🆘 Help", callback_data="help"), 
            InlineKeyboardButton("👩‍💻 Developer", callback_data="developer")
        ],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                    text="Welcome to the Go Tiny Tools Bot!",
                                    reply_markup=reply_markup)
async def categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📝 Writing Tools", callback_data="writing_tools"),
            InlineKeyboardButton("🤖 AI Tool", callback_data="ai_category"),
            InlineKeyboardButton("🧑🏼‍💻Coding Tools", callback_data="coding_category"),
        ],
        [
            InlineKeyboardButton("⏱️ Productivity Tools", callback_data="productivity_category"),
            InlineKeyboardButton("😄 Fun Tools", callback_data="fun_tools"),
            InlineKeyboardButton("🎨 Multimedia Tools", callback_data="multimedia_tools"),
        ],
        [
            InlineKeyboardButton("ℹ️ Information Tools", callback_data="information_tools"),
            InlineKeyboardButton("🔐 Password Tools", callback_data="password_tools"),
            InlineKeyboardButton("🧮 Math Tools", callback_data="search_tools"),

        ],
        [
            InlineKeyboardButton("🔄 Conversion Tools", callback_data="conversion_tools"),
            InlineKeyboardButton("🔍 Search Tools", callback_data="search_tools"),
            InlineKeyboardButton("🔍 Request Tool", callback_data="request_tools"),
        ],
        [
            InlineKeyboardButton("🔙 Back", callback_data="back")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                    text="Welcome to the Go Tiny Tools 🗂️ Categories!",
                                    reply_markup=reply_markup)

async def tools(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🗂️ Categories", callback_data="categories"),
            InlineKeyboardButton("Tools", callback_data="tools")
        ],
        [
            InlineKeyboardButton("🆘 Help", callback_data="help"), 
            InlineKeyboardButton("Developer", callback_data="developer")
        ],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                    text="Welcome to the Go Tiny Tools!",
                                    reply_markup=reply_markup)
                                
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Opening help center...")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Go Tiny! Here's how I can assist you\n\n 🗂️ Categories:\n\n1. Password Generator\n2. AI Tools\n\nUse /start to get started!\n\n Commands:\n/start - Starts the bot\n/help - Show this help message\nDeveloper:\n\n@StealthWizard")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://t.me/GoTinyToolsBotHelpCenter")

async def developer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Opening developer's Telegram account...")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://t.me/StealthWizard")

async def button_clicked(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "categories":
        keyboard = [
            [
                InlineKeyboardButton("📝 Writing Tools", callback_data="writing_tools"),
                InlineKeyboardButton("🤖 AI Tool", callback_data="ai_category"),
                InlineKeyboardButton("🧑🏼‍💻Coding Tools", callback_data="coding_category"),
            ],
            [
                InlineKeyboardButton("⏱️ Productivity Tools", callback_data="productivity_category"),
                InlineKeyboardButton("😄 Fun Tools", callback_data="fun_tools"),
                InlineKeyboardButton("🎨 Multimedia Tools", callback_data="multimedia_tools"),
            ],
            [
                InlineKeyboardButton("ℹ️ Information Tools", callback_data="information_tools"),
                InlineKeyboardButton("🔐 Password Tools", callback_data="password_tools"),
                InlineKeyboardButton("🧮 Math Tools", callback_data="search_tools"),

            ],
            [
                InlineKeyboardButton("🔄 Conversion Tools", callback_data="conversion_tools"),
                InlineKeyboardButton("🔍 Search Tools", callback_data="search_tools"),
                InlineKeyboardButton("🔍 Request Tool", callback_data="request_tools"),
            ],
            [
                InlineKeyboardButton("🔙 Back", callback_data="back")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Choose a category:", reply_markup=reply_markup)
    elif query.data == "tools":
        keyboard = [
            [InlineKeyboardButton("Password Generator", callback_data="password_generator")],
            InlineKeyboardButton("🔙 Back", callback_data="back")
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Tools:", reply_markup=reply_markup)
    elif query.data == "ai_category":
        keyboard = [
            [InlineKeyboardButton("Content Shortener", callback_data="content_shortener")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="AI Tools:", reply_markup=reply_markup)
    elif query.data == "coding_category":
        keyboard = [
            [InlineKeyboardButton("Python bug buster", callback_data="python_bug_buster")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Coding Tools:", reply_markup=reply_markup)
    elif query.data == "python_bug_buster":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide the Python code to be fixed:")
        context.user_data["tool"] = "python_bug_buster"
    elif query.data == "content_shortener":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide the content to be shortened:")
        context.user_data["tool"] = "content_shortener"
    elif query.data == "help":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Opening help center...")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Go Tiny! Here's how I can assist you\n\n 🗂️ Categories:\n\n1. Password Generator\n2. AI Tools\n\nUse /start to get started!\n\n Commands:\n/start - Starts the bot\n/help - Show this help message\nDeveloper:\n\n@StealthWizard")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://t.me/GoTinyToolsBotHelpCenter")
    elif query.data == "developer":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Opening developer's Telegram account...")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://t.me/StealthWizard")
    elif query.data == "back":
        keyboard = [
        [
            InlineKeyboardButton("🗂️ Categories", callback_data="categories"),
            InlineKeyboardButton("Tools", callback_data="tools")
        ],
        [
            InlineKeyboardButton("🆘 Help", callback_data="help"), 
            InlineKeyboardButton("👩‍💻 Developer", callback_data="developer")
        ],
        
    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Welcome to the Tiny Tools Bot!", reply_markup=reply_markup)
    elif query.data == "password_category":
        keyboard = [
            [InlineKeyboardButton("Password Generator", callback_data="password_generator")],
            InlineKeyboardButton("🔙 Back", callback_data="back")
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Password Tools:", reply_markup=reply_markup)
    elif query.data == "password_generator":
        await password_generator(update, context)
        await query.edit_message_text(text="Password generated successfully!")

async def text_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "tool" in context.user_data and context.user_data["tool"] == "content_shortener":
        content = update.message.text
        shortened_content = shorten_content(content)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{shortened_content}")
        context.user_data.pop("tool", None)
    elif "tool" in context.user_data and context.user_data["tool"] == "python_bug_buster":
        code = update.message.text
        fixed_code = fix_python_bug(code)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{fixed_code}")
        context.user_data.pop("tool", None)

async def password_generator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    length = 12  # Default password length
    if context.args:
        try:
            length = int(context.args[0])
        except ValueError:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid length. Using default (12).")
    password = generate_password(length)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your generated password: {password}")

def main():
    application = ApplicationBuilder().token(Token).build()

    # Add command handlers
    start_handler = CommandHandler('start', start)
    categories_handler = CommandHandler('categories', categories)
    tools_handler = CommandHandler('tools', tools)
    password_generator_handler = CommandHandler('password_generator', password_generator)
    help_handler = CommandHandler('help', help)
    developer_handler = CommandHandler('developer', developer)
    button_handler = CallbackQueryHandler(button_clicked)
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, text_received)

    application.add_handler(start_handler)
    application.add_handler(categories_handler)
    application.add_handler(tools_handler)
    application.add_handler(password_generator_handler)
    application.add_handler(help_handler)
    application.add_handler(developer_handler)
    application.add_handler(button_handler)
    application.add_handler(text_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
