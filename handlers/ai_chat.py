from openai import OpenAI
from telegram.ext import MessageHandler, filters

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def handle_ai_chat(update, context):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": update.message.text}]
    )
    await update.message.reply_text(response.choices[0].message.content)

ai_chat_handler = MessageHandler(filters.text & ~filters.command, handle_ai_chat)