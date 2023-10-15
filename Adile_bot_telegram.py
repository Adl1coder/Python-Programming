from typing import Final
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# I must change token for security, u can use ur token
token = '654192375333330:AAERUUXfwxGVRF8RJnJFwYSvPDn7otiFCm0'
bot_username: Final = '@Adilegungorbot'


# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am assistant bot telling about Adile ')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am assistant bot telling about Adile ')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Adile company')


# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'Hello!'
    if 'How are you' in processed:
        return 'I am good, thanks!'
    if 'I love python' in processed:
        return 'Remember me ok?'

    return 'I do not understand what you wrote...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(token).build()

# Commands
app.add_handler(CommandHandler('start', start_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('custom', custom_command))

# Messagesc
app.add_handler(MessageHandler(filters.TEXT, handle_message))

# Errors
app.add_error_handler(error)

# Polls the bot
print('Polling...')
app.run_polling(poll_interval=3)


# print('Completed !')
