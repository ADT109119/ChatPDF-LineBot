from Model.BaseModel import BaseModel

class LlmModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.filed = ['id', 'name', 'base_url', 'token']
        self.table = 'llm_model'

    def get_all_models(self):
        return self.sql_query(f"SELECT id, name from {self.table}")