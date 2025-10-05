import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# টোকেনটি আমরা পরবর্তীতে 'RENDER' এ সেট করব।
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN") 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # /start কমান্ড দিলে এই মেসেজটি রিপ্লাই হবে
    await update.message.reply_text('স্বাগতম! আপনার বট চালু আছে।')

def main() -> None:
    if not TOKEN:
        print("টোকেন পাওয়া যায়নি। Render-এ টোকেন সেট করুন।")
        return

    # বট অ্যাপ্লিকেশন তৈরি এবং টোকেন ব্যবহার
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES) 

if __name__ == "__main__":
    main()
