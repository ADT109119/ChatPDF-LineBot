from Model.BaseModel import BaseModel
from Model.Setting import Setting
setting = Setting()
class KnowledgeBase(BaseModel):
    def __init__(self):
        super().__init__()
        self.filed = ['id', 'line_id', 'name', 'model','temperature', 'score_threshold', 'search_item_limit']
        self.table = 'knowledge_base'

    def get_setting(self, id, line_id):
        result = self.sql_query(f"SELECT * FROM {self.table} WHERE id = ? AND line_id = ?", (id, line_id,))[0]

        return {
            "id": result[0],
            "name": result[2],
            "base_url": setting.BASE_URL[result[3]],
            "api_key": setting.API_KEY[result[3]],
            # "model": setting.MODEL_NAME[result[3]],
            "model": result[3],
            "temperature": result[4],
            "score_threshold": result[5],
            "search_item_limit": result[6]
        }
    
    def get_list(self, line_id):
        result = self.sql_query(f"SELECT * FROM {self.table} WHERE line_id = ?", (line_id,))
        return result

    def updateData(self, id, line_id, data: dict):
        self.sql_query(f"UPDATE {self.table} SET id=?, name=?, model=?, temperature=?, score_threshold=?, search_item_limit=? WHERE id = ? AND line_id = ?", 
                       (data['id'], data['name'], data['model'], data['temperature'], data['score_threshold'], data['search_item_limit'], id, line_id,))
        
    def deleteData(self, id, line_id):
        self.sql_query(f"DELETE FROM {self.table} WHERE id = ? AND line_id = ?", (id, line_id,))

knowledgeBase = KnowledgeBase()