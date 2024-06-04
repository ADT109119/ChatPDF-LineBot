import config.line_reply_template as config
from Model.Setting import setting
from Model.UploadedFiles import uploadedFiles

import time

from Service.upload_file import calc_total_size

def replay_info(line_id):
    temp = config.INFO_TEMPLATE
    temp = temp.replace("{$VERSION}", setting.VERSION)
    temp = temp.replace("{$FILE_AMOUNT}", str(uploadedFiles.get_file_amount(line_id)))
    temp = temp.replace("{$FILE_SIZE_LIMIT}", setting.byte_to_kb_or_mb(setting.FILE_MAX_SIZE))
    temp = temp.replace("{$USED_SPACE}", f"{setting.byte_to_kb_or_mb(calc_total_size(line_id))}/{setting.byte_to_kb_or_mb(setting.SPACE_PER_USER)}")
    temp = temp.replace("{$USED_SPACE_PERCENTAGE}", str(calc_total_size(line_id)/setting.FILE_MAX_SIZE * 100)+"%")
    temp = temp.replace("{$MAX_CHAT_HISTORY}", str(setting.MAX_CHAT_HISTORY))
    return temp
    
def replay_help():
    t = time.time()
    tt = time.localtime(t)
    temp = config.HELP_TEMPLATE
    temp = temp.replace("{$TIME}", f"{tt.tm_year}{tt.tm_mon}{tt.tm_mday}")
    return temp
    
def replay_about_me():
    return config.ABOUT_ME