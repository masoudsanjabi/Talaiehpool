
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import random

# اطلاعات قابل تنظیم توسط ادمین
lottery_config = {
    'free': 10,
    'fifty': 10,
    'thirty': 50
}

admin_ids = ["@Kswimmers", "@Masoudsanjabiii"]

users = ['user' + str(i) for i in range(1, 101)]

def lottery(update: Update, context: CallbackContext):
    free_count = lottery_config['free']
    fifty_count = lottery_config['fifty']
    thirty_count = lottery_config['thirty']

    free = random.sample(users, free_count)
    remaining = list(set(users) - set(free))
    fifty = random.sample(remaining, min(fifty_count, len(remaining)))
    remaining = list(set(remaining) - set(fifty))
    thirty = random.sample(remaining, min(thirty_count, len(remaining)))

    message = "🎁 قرعه‌کشی امروز:\n"
    message += f"🎫 رایگان: {', '.join(free)}\n"
    message += f"🎟️ ۵۰٪ تخفیف: {', '.join(fifty)}\n"
    message += f"🎫 ۳۰٪ تخفیف: {', '.join(thirty)}"

    update.message.reply_text(message)

def hours(update: Update, context: CallbackContext):
    update.message.reply_text("🕒 ساعت کاری هنوز ثبت نشده. لطفاً بعداً بررسی کنید.")

def classes(update: Update, context: CallbackContext):
    update.message.reply_text("📚 لیست کلاس‌ها هنوز وارد نشده است.")

def signup(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("پرداخت و ثبت‌نام", url='https://your-payment-link.com')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("برای ثبت‌نام روی دکمه زیر کلیک کنید:", reply_markup=reply_markup)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("""
سلام! به ربات استخر طلائیه خوش آمدید 🌊
گزینه‌های زیر را انتخاب کنید:
/lottery 🎁 قرعه‌کشی امروز
/hours 🕒 ساعت کاری
/classes 📚 کلاس‌های آموزشی
/signup 💳 ثبت‌نام و پرداخت
    """)

if __name__ == '__main__':
    app = ApplicationBuilder().token("7930450953:AAG_3_XtgJJj1D-tR-w02xtaHgJqB28-F4s").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hours", hours))
    app.add_handler(CommandHandler("classes", classes))
    app.add_handler(CommandHandler("lottery", lottery))
    app.add_handler(CommandHandler("signup", signup))
    print("🤖 ربات استخر طلائیه در حال اجراست...")
    app.run_polling()
