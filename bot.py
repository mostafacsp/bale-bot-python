#import bale
#from bale import Bot , Message

#bot=Bot(token="444444444444")

#@bot.message_handler(commands=['start'])
#def send_welcome(message:Message):
#    text = "berongggg man"
 #   bot.reply(message,TextMessage(text))
#if __name__ == "__main__":
#    bot.run()
from bale import Bot, Message
from bale import Bot, Message, User
import asyncio
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token="اااااااااااااا")
user_states = {}

class UserState:
    def __init__(self, user_id):
        self.user_id = user_id
        self.state = "MAIN_MENU"
        self.data = {}

@bot.event
async def on_message(message: Message):
    text = message.content
    try:
        user_id = message.author.id

        # ایجاد وضعیت کاربر اگر وجود ندارد
        if user_id not in user_states:
            user_states[user_id] = UserState(user_id)

        user_state = user_states[user_id]
        text = message.content

        logger.info(f"📩 پیام از {message.author.username}: {text}")
    
        if text == "/start":
            await send_welcome_message(message)

        elif text == "/menu" or text == "📋 منو":
            await show_main_menu(message)

        elif text == "پروفایل" or text== "1":
            await show_profile(message)

        elif text == "📊 خدمات" or text=="2":
            await show_services(message)

        elif text == "📞 پشتیبانی" or text=="3":
            await show_support(message)

        elif text == "ℹ️ درباره ما" or text=="4":
            await show_about(message)

        elif text == "🔙 بازگشت" or text=="0":
            await show_main_menu(message)

        elif text.startswith("/"):
            await message.reply("❌ دستور نامعتبر! لطفا از منو استفاده کنید.")

        else:
            # پاسخ به پیام‌های معمولی
            await handle_regular_message(message, text)

    except Exception as e:
        logger.error(f"❌ خطا در پردازش پیام: {e}")
        await message.reply("⚠️ خطایی رخ داد! لطفا مجددا تلاش کنید.")

async def send_welcome_message(message: Message):
    """ارسال پیام خوشآمدگویی"""
    welcome_text = """
    🌟 *به ربات ما خوش آمدید! 🌟

    🤖 من یک ربات هوشمند هستم که می‌تونم در زمینه‌های مختلف به شما کمک کنم.

    📋 از طریق منوی زیر می‌تونید با امکانات ربات آشنا بشید.
    """

    await message.reply(welcome_text)
    await show_main_menu(message)

async def show_main_menu(message: Message):
    """نمایش منوی اصلی"""
    menu_text = """
    🏠 منوی اصلی

    لطفا یکی از گزینه‌های زیر را انتخاب کنید:

    👤 پروفایل یا شماره 1- مشاهده اطلاعات حساب
    📊 خدمات یا شماره 2 - مشاهده خدمات ربات
    📞 پشتیبانی یا شماره 3 - ارتباط با پشتیبانی
    ℹ️ درباره ما یا شماره 4 - اطلاعات درباره ربات
    """

    await message.reply(menu_text)

async def show_profile(message: Message):
    """نمایش پروفایل کاربر"""
    user = message.author
    profile_text = f"""
    👤 پروفایل کاربر

    🆔 شناسه: `{user.id}`
    📛 نام: {user.first_name}
    📧 یوزرنیم: @{user.username if user.username else 'ندارد'}
    👥 وضعیت: کاربر عادی
    ⭐ امتیاز: ۱۰۰

    💰 اعتبار: ۰ تومان
    """

    await message.reply(profile_text)

async def show_services(message: Message):
    """نمایش خدمات"""
    services_text = """
    🛍️ خدمات ربات

    🔹 خدمات رایگان:
    ✅ دریافت اطلاعات کاربر
    ✅ راهنمایی و پشتیبانی
    ✅ اطلاع‌رسانی

    🔹 خدمات ویژه:
    ⭐ مدیریت پیشرفته
    ⭐ گزارش‌گیری حرفه‌ای
    ⭐ اتوماسیون کاری

    💰 برای اطلاعات بیشتر با پشتیبانی تماس بگیرید.
    """

    await message.reply(services_text)

async def show_support(message: Message):
    """نمایش اطلاعات پشتیبانی"""
    support_text = """
    📞 پشتیبانی

    🕒 ساعت پاسخگویی: ۹ صبح تا ۶ عصر
    📧 ایمیل: support@example.com
    📱 تلفن: ۰۲۱-۱۲۳۴۵۶۷۸
    🌐 وبسایت: example.com

    💬 برای ارتباط مستقیم لطفا پیام خود را ارسال کنید.
    """

    await message.reply(support_text)

async def show_about(message: Message):
    """نمایش اطلاعات درباره ربات"""
    about_text = """
    ℹ️ درباره ما

    🤖 ربات هوشمند خدمات*
     🎯 ماموریت:
    ارائه بهترین خدمات به کاربران

    ⭐ ویژگی‌ها:
    - سرعت بالا
    - امنیت قوی
    - پشتیبانی ۲۴ ساعته
    - رایگان

    👨‍💻 توسعه‌دهنده:
    تیم فناوری اطلاعات

    📅 ورژن:* ۱.۰.۰
    """

    await message.reply(about_text)
async def handle_regular_message(message: Message, text: str):
    """پردازش پیام‌های معمولی کاربر"""

    # پاسخ به سلام
    if any(word in text.lower() for word in ['سلام', 'hello', 'hi', 'salam']):
        await message.reply(f"سلام {message.author.first_name}! 😊\nچطور می‌تونم کمک کنم؟")

    # پاسخ به احوالپرسی
    elif any(word in text.lower() for word in ['حالت', 'چطوری', 'خوبی']):
        await message.reply("ممنون! من خوبم 😊\nشما چطور؟")

    # پاسخ به تشکر
    elif any(word in text.lower() for word in ['ممنون', 'مرسی', 'تشکر']):
        await message.reply("خواهش می‌کنم! 😊\nاگر سوال دیگه‌ای دارید بپرسید.")

    # پاسخ به خداحافظی
    elif any(word in text.lower() for word in ['خداحافظ', 'بای', 'bye']):
        await message.reply("خداحافظ! 🙋‍♂️️\nمنتظر پیام بعدی شما هستم.")
        
     #پاسخ به فحش 
    elif any(word in text.lower() for word in ['خر' ,'سگ','لاشی','بیشعور','نامرد ']):
        await message.reply("چقدر پررویی تو گمشو بابا دم کونتو بگیر ")

    else:
        # پاسخ پیش‌فرض
        await message.reply(
            f"پیام شما دریافت شد: \"{text}\"\n\n"
            "برای دیدن امکانات ربات از دستور /menu استفاده کنید."
        )


@bot.event
async def on_ready():
    print("ربات با موفقیت راه اندازی شد")


bot.run()