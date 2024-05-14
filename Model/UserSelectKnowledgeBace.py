from Model.BaseModel import BaseModel

class UserSelectKnowledgeBace(BaseModel):
    def __init__(self):
        super().__init__()
        self.filed = ['line_id', 'knowledge_base_id']
        self.table = 'user_select_knowledge_base'

    def getData(self, user_id):
        return self.sql_query(f"SELECT * FROM {self.table} WHERE line_id=?", (user_id, ))
    
    def changeSelected(self, line_id: str, knowledge_base_id: int):
        if len(self.getData(line_id)) == 0:
            self.sql_query(f"INSERT INTO {self.table} (line_id, knowledge_base_id) VALUES (?,?)", (line_id, knowledge_base_id, ))
        else:
            self.sql_query(f"UPDATE {self.table} SET knowledge_base_id=? WHERE line_id=?", (knowledge_base_id, line_id, ))

userSelectKnowledgeBace = UserSelectKnowledgeBace()