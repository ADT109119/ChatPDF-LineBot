from Model.UploadedFiles import uploadedFiles
from Model.Setting import setting

from fastapi import UploadFile, HTTPException

import os
import uuid
import datetime

def upload_file(line_id, file: UploadFile):

        file_name = file.filename

        # 辨識檔案類型
        if file_name.split(".")[-1] not in setting.ALLOW_FILE_TYPE:
            raise HTTPException(status_code=400, detail="unsupport file type")
        
        today = datetime.date.today()
        unique_id = str(uuid.uuid4())

        file_path = f'./db/files/{today.year}/{today.month}/{today.day}/{unique_id}_{file_name}'

        # 獲取目錄路徑
        dir_path = os.path.dirname(file_path)

        # 如果目錄不存在,則創建它
        if not os.path.exists(dir_path):
            try:
                os.makedirs(dir_path)
            except OSError as e:
                if e.errno != os.errno.EEXIST:
                    raise  # 如果不是文件已存在的錯誤,則重新引發異常

        try:
            with open(file_path, 'wb') as fd:
                content = file.file.read()
                if len(content) > setting.FILE_MAX_SIZE:
                    raise Exception("file size too large")
                
                # 檢查空間是否足夠
                total_size = calc_total_size(line_id)
                # file_list = uploadedFiles.get_all_files_list(line_id)
                # for f in file_list:
                #     total_size += os.stat(f[3]).st_size
                # print(total_size)
                if total_size+len(content) > setting.SPACE_PER_USER:
                    raise Exception("space limit reached")

                fd.write(content)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

        try:
            # 寫入資料庫
            return uploadedFiles.upload_file(line_id, file_name, file_path)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="error")
                # return self.sql_query('INSERT INTO uploaded_files (id, line_id, file_name, file_path) VALUES (null, ?, ?, ?)', (line_id, file_name, file_path, ), True)
        

def delete_file(file_id, line_id):
    try:
        # 獲取檔案路徑
        _, file_path = uploadedFiles.get_file(file_id, line_id)[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail="file does not exist")

    try:
        # 刪除檔案
        if os.path.exists(file_path):
            os.remove(file_path)
        # 刪除資料庫中的資料
        uploadedFiles.delete_file(file_id, line_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="error")

def calc_total_size(line_id):
    total_size = 0
    file_list = uploadedFiles.get_all_files_list(line_id)
    for f in file_list:
        total_size += os.stat(f[3]).st_size

    return total_size
