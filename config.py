
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7422394676:AAG6JFLuOVfrAZtvhkfEWprrRORuNx_dwtg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9698652"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b354710ab18b84e00b65c62ba7a9c043")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002385560786"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2125687935"))

#Port
PORT = os.environ.get("PORT", "8008")

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://test:2003@cluster0.fj2wn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "test")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "0"))

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "inshorturl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "c6afac58d50114bfb3e1c6aad64f90e0591bf77e")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "36000")) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/delight_link/2")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002084114293"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001802782627"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002115482280"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/Rv_.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/Rvc.jpg")

QR_PIC = os.environ.get("QR_PIC", "https://envs.sh/RvG.jpg")

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "2125687935").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>ʙʏ @DelightNetwork</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('FALSE', "True") == "True" else False

#==========================(BUY PREMIUM)====================#

PREMIUM_BUTTON = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
)

PREMIUM_BUTTON2 = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
) 

OWNER_TAG = os.environ.get("OWNER_TAG", "delight_admin_bot")

#UPI ID
UPI_ID = os.environ.get("UPI_ID", "@delight_admin_bot")

#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://t.me/paymentbot6/2")

#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/delight_admin_bot")



#Time and its price

#7 Days
PRICE1 = os.environ.get("PRICE1", "69 rs")

#1 Month
PRICE2 = os.environ.get("PRICE2", "130 rs")

#3 Month
PRICE3 = os.environ.get("PRICE3", "330 rs")

#6 Month
PRICE4 = os.environ.get("PRICE4", "700 rs")

#1 Year
PRICE5 = os.environ.get("PRICE5", "1300 rs")


#===================(END)========================#


#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("True", True) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Sharing Bot!"






ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
