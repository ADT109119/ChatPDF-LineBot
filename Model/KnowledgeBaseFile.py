from Model.BaseModel import BaseModel

class KnowledgeBaseFile(BaseModel):
    def __init__(self):
        super().__init__()
        self.filed = ['knowledge_base_id', 'file_id', 'active']
        self.table = 'knowledge_base_file'

    def get_all_files(self, line_id, knowledge_base_id):
        return self.sql_query(f'SELECT f.id, f.file_name, f.file_path, kbf.active FROM {self.table} AS kbf INNER JOIN knowledge_base AS kb ON kb.id=kbf.knowledge_base_id INNER JOIN uploaded_files AS f ON f.id=kbf.file_id WHERE knowledge_base_id = ? AND kb.line_id = ?', (knowledge_base_id, line_id, ))
    
    def add_file_to_knowledge_base(self, line_id, knowledge_base_id, file_id):
        # values = ', '.join(['?'] * len(file_ids))

        return self.sql_query(f"""
        INSERT INTO knowledge_base_file (knowledge_base_id, file_id)
        SELECT kb.id, uf.id
        FROM knowledge_base kb
        CROSS JOIN uploaded_files uf
        WHERE kb.id = ?
            AND kb.line_id = ?
            AND uf.line_id = ?
            AND uf.id IN (?)
        """, (knowledge_base_id, line_id, line_id, file_id,))
    
    def setActive(self, line_id, knowledge_base_id, file_id, active):
        return self.sql_query(f"""
        UPDATE {self.table} SET active =? 
        WHERE knowledge_base_id=(SELECT id FROM knowledge_base WHERE id=? AND line_id=?)
            AND file_id=(SELECT id FROM uploaded_files WHERE id=? AND line_id=?)
        """, (active, knowledge_base_id, line_id, file_id, line_id))
    
    def delete_file_from_knowledge_base(self, knowledge_base_id, file_id, line_id):
        return self.sql_query(f"""
        DELETE FROM {self.table}
        WHERE knowledge_base_id = (SELECT id FROM knowledge_base WHERE id = ? AND line_id = ?)
          AND file_id = (SELECT id FROM uploaded_files WHERE id = ? AND line_id = ?)
        """, (knowledge_base_id, line_id, file_id, line_id))

knowledgeBaseFile = KnowledgeBaseFile()