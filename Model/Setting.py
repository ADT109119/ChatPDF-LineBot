import os
from dotenv import load_dotenv
load_dotenv(override=True)

class Setting:
    def __init__(self):
        self.LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN") or os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")
        self.LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET") or os.getenv("LINE_CHANNEL_SECRET", "")
        self.LINE_LIFF_ID = os.environ.get("LINE_LIFF_ID") or os.getenv("LINE_LIFF_ID", "")
        self.LINE_LOGIN_CHANNEL_ID = os.environ.get("LINE_LOGIN_CHANNEL_ID") or os.getenv("LINE_LOGIN_CHANNEL_ID", "")
        
        self.EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL") or os.getenv("EMBEDDING_MODEL")
        self.EMBEDDING_DEVICE = os.environ.get("EMBEDDING_DEVICE") or os.getenv("EMBEDDING_DEVICE")

        self.MODEL_NAME = os.environ.get("MODEL_NAME", "").split("|") or os.getenv("MODEL_NAME", "").split("|")
        self.BASE_URL = os.environ.get("BASE_URL", "").split("|") or os.getenv("BASE_URL", "").split("|")
        self.API_KEY = os.environ.get("API_KEY", "").split("|") or os.getenv("API_KEY", "").split("|")

        self.FILE_MAX_SIZE = self.space_conversion(os.environ.get("FILE_MAX_SIZE") or os.getenv("FILE_MAX_SIZE", "5MB"))
        self.SPACE_PER_USER = self.space_conversion(os.environ.get("SPACE_PER_USER") or os.getenv("SPACE_PER_USER", "200MB"))

        self.ALLOW_FILE_TYPE = os.environ.get("ALLOW_FILE_TYPE", "pdf,csv,txt").split(",") or os.getenv("ALLOW_FILE_TYPE", "pdf,csv,txt").split(",")

        self.MAX_CHAT_HISTORY = int(os.environ.get("MAX_CHAT_HISTORY") or os.getenv("MAX_CHAT_HISTORY", "5"))


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