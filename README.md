# Go Tiny Bot

Go Tiny Tools Bot is a powerful and versatile Telegram bot that provides a collection of useful tools for users. It offers a wide range of features categorized into different sections, including writing tools, conversion tools, math tools, coding tools, multimedia tools, productivity tools, information tools, fun tools, AI tools, and password tools.

## Features

### Writing Tools
- Grammar Checker
- Paraphrasing Tool
- Text Summarizer
- Rhyme Generator
- Story Idea Generator

### Conversion Tools
- Unit Converter (Length, Weight, Temperature, etc.)
- Currency Converter
- File Converter (PDF to Word, Word to PDF, etc.)
- Case Converter (uppercase, lowercase, etc.)
- Timestamp Converter (Unix, ISO, etc.)

### Math Tools
- Scientific Calculator
- Equation Solver
- Prime Number Checker
- Factorial Calculator
- Geometric Calculator (Area, Volume, etc.)

### Coding Tools
- Python Bug Buster ✅
- Code Formatter/Beautifier
- Code Minifier/Obfuscator
- Code Snippet Sharing/Collaboration
- Regular Expression Tester
- JSON/XML/YAML Formatter

### Multimedia Tools
- Image Resizer
- Image Compressor
- Video Trimmer
- Audio Converter
- QR Code Generator

### Productivity Tools
- To-Do List Manager
- Pomodoro Timer
- URL Shortener
- Reminder/Alarm Scheduler
- Notes/Clipboard Manager

### Information Tools
- Wikipedia Lookup
- Word Definition Lookup
- Stock Market Updates
- Weather Forecasts
- IP Address Lookup

### Fun Tools
- Joke Generator
- Riddle Solver
- Horoscope Reader
- Fortuneteller
- Madlibs Generator

### AI Tools
- Content Shortener✅
- Text Summarizer
- Language Translator

### Password Tools
- Password Generator✅

## Chat with the Bot

You can start chatting with the Go Tiny Tools Bot right away by clicking the link below:

[![Chat with the Bot](https://img.shields.io/badge/Chat%20with%20the%20Bot-blue?style=for-the-badge)](https://t.me/gotinybot)

## Installation
Clone the repository:
  ```bash
  git clone https://github.com/Codewithshagbaor/Go-Tiny.git
  ```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
Set up the necessary configurations, such as the Telegram bot token and API keys (if applicable).
Run the bot:
```bash
python main.py
```
# Changelog

## [Unreleased]
### Added
- Implemented the `handle_tool` function in the `text_received` handler to handle text input for various tools.
- Added support for processing user input based on subscription status (free or paid) and token balance.
- Added functionality to deduct tokens from the user's balance when using paid tools with a free subscription.

### Changed
- Modified the `text_received` handler to retrieve user data from the database and update the `context.user_data` dictionary with the latest subscription status, token balance, and message count.
- Refactored the code to handle different tools using the `handle_tool` function instead of separate conditions.

### Fixed
- Resolved the `KeyError: 'subscription'` issue by initializing the `subscription` key with a default value when retrieving user data from the database.

## [Previous Versions]
### Added
- Initial implementation of the Telegram bot with various features and tools.
- Support for categories, inline keyboards, and command handlers.
- Integration with external APIs and tools for functionality like content shortening, grammar checking, password generation, and information lookup.
- Database integration using SQLite to store user data.
- Advertisement display functionality based on user subscription status and message count.

### Changed
- Refactored code structure and organization.
- Updated documentation and help messages.

### Fixed
- Bug fixes and stability improvements.

## Contributing
Contributions are welcome! If you find any bugs, have feature requests, or want to contribute improvements, please open an issue or submit a pull request. Make sure to follow the contribution guidelines.
## License
This project is licensed under the MIT License.

## Acknowledgments
[python-telegram-bot](https://github.com/python-telegram-bot) - The Python library used for interacting with the Telegram Bot API.

[Anthropic](https://www.anthropic.com) - The AI platform used for content shortening and other AI-powered features.

Contact
For any questions or inquiries, please contact the project maintainer.

[![Chat with the Project Maintainer](https://img.shields.io/badge/Chat%20with%20the%20Project%20Maintainer-blue?style=for-the-badge)](mailto:dxtlive@gmail.com)
