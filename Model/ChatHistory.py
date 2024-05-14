from Model.BaseModel import BaseModel
from Model.Setting import setting

class ChatHistory(BaseModel):
    def __init__(self):
        super().__init__()
        self.filed = ['time', 'line_id', 'user_message', 'bot_message']
        self.table = 'chat_history'

    def clear(self, line_id):
        return self.sql_query('DELETE FROM chat_history WHERE line_id =?', (line_id,))
    
    def get_history(self, line_id):
        return self.sql_query('SELECT user_message, bot_message FROM chat_history WHERE line_id =? ORDER BY time DESC LIMIT ?', (line_id, setting.MAX_CHAT_HISTORY,))

chatHistory = ChatHistory()