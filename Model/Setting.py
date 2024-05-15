import os
from dotenv import load_dotenv

if not os.getenv("IN_DOCKER", ""):
    load_dotenv(override=True)

class Setting:
    def __init__(self):
        self.LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "YOUR_LINE_CHANNEL_ACCESS_TOKEN")
        self.LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", "YOUR_LINE_CHANNEL_SECRET")
        self.LINE_LIFF_ID = os.environ.get("LINE_LIFF_ID") or os.getenv("LINE_LIFF_ID", "YOUR_LINE_LIFF_ID")
        self.LINE_LOGIN_CHANNEL_ID = os.getenv("LINE_LOGIN_CHANNEL_ID", "YOUR_LINE_LOGIN_CLIENT_ID")
        
        self.EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
        self.EMBEDDING_DEVICE = os.getenv("EMBEDDING_DEVICE", "cpu")

        self.MODEL_NAME = os.getenv("MODEL_NAME", "llama3-8b-8192|gpt-3.5-turbo|gpt-4-1106-preview").split("|")
        self.BASE_URL = os.getenv("BASE_URL", "https://api.groq.com/openai/v1|https://api.openai.com/v1|https://api.openai.com/v1").split("|")
        self.API_KEY = os.getenv("API_KEY", "API_KEY_1|API_KEY_2|API_KEY_3").split("|")

        self.FILE_MAX_SIZE = self.space_conversion(os.getenv("FILE_MAX_SIZE", "5MB"))
        self.SPACE_PER_USER = self.space_conversion(os.getenv("SPACE_PER_USER", "200MB"))

        self.ALLOW_FILE_TYPE = os.getenv("ALLOW_FILE_TYPE", "pdf,csv,txt").split(",")

        self.MAX_CHAT_HISTORY = int(os.getenv("MAX_CHAT_HISTORY", "5"))


    def space_conversion(self, space):
        space = space.upper()
        space = space.replace("B", "")
        if 'K' in space:
            space = float(space.replace("K", ""))
            return int(space * 1024)
        
        if 'M' in space:
            space = float(space.replace("M", ""))
            return int(space * 1024 * 1024)
        
        if 'G' in space:
            space = float(space.replace("G", ""))
            return int(space * 1024 * 1024 * 1024)
        
        if 'T' in space:
            space = float(space.replace("T", ""))
            return int(space * 1024 * 1024 * 1024 * 1024)
        
        return 0
    

setting = Setting()