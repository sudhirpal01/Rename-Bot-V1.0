import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21811923")

API_HASH = os.environ.get("API_HASH", "d66b936aaf05e15f7fb0badc901b55b4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6711951729:AAG9MTQeNAWJ1YiI1bF9CJSL3c9Kf1Xaz4A") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Anime_Shrinnes") 

DB_NAME = os.environ.get("DB_NAME","kakashi")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://kakashi:kakashi@cluster0.njeic9y.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/34d01864d06b6b3921c6a.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5842887550').split()]

PORT = os.environ.get("PORT", "8080")
