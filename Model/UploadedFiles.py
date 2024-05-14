from Model.BaseModel import BaseModel
import time
import random
import datetime
import os
from fastapi import UploadFile
import uuid
from Model.Setting import setting
from fastapi import HTTPException

class UploadedFiles(BaseModel):
    def __init__(self):
        super().__init__()
        self.filed = ['id', 'line_id', 'file_name', 'file_path']
        self.table = 'uploaded_files'

    def get_file(self, id, line_id):
        return self.sql_query('SELECT file_name, file_path FROM uploaded_files WHERE id =? AND line_id =?', (id, line_id, ))

    def get_all_files_list(self, line_id):
        return self.sql_query('SELECT * FROM uploaded_files WHERE line_id = ?', (line_id, ))
    
    async def upload_file(self, line_id, filename, filepath):
        try:
            return self.sql_query('INSERT INTO uploaded_files (id, line_id, file_name, file_path) VALUES (null, ?, ?, ?)', (line_id, filename, filepath, ), True)
        except Exception as e:
            raise {"error": str(e)}
        
    def delete_file(self, file_id, line_id):
        return self.sql_query('DELETE FROM uploaded_files WHERE id =? AND line_id =?', (file_id, line_id, ))

        
uploadedFiles = UploadedFiles()