from fastapi import Request, HTTPException, APIRouter

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction

import os

from Model.Setting import setting
from Model.UserSelectKnowledgeBace import userSelectKnowledgeBace
from Model.ChatHistory import chatHistory

from Service.llm import chat_llm

line_router = APIRouter()
line_bot_api = LineBotApi(setting.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(setting.LINE_CHANNEL_SECRET) 


@line_router.post("/callback")
async def callback(request: Request):
    signature = request.headers["X-Line-Signature"]
    body = await request.body()
    try:
        handler.handle(body.decode(), signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Missing Parameters")
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handling_message(event):

    
    if isinstance(event.message, TextMessage):

        
        user_message = event.message.text
        line_id = event.source.user_id
        QuickReplyButtons = [
            QuickReplyButton(
                action=MessageAction(label="繼續",text="繼續")
            ),
            QuickReplyButton(
                action=MessageAction(label="清除對話",text="/clear")
            )
        ]

        if user_message[0] == "/":
            func, args = parseMessage(user_message)
            if func == "select":
                try:
                    userSelectKnowledgeBace.changeSelected(line_id, args)
                    reply_msg = "已切換知識庫"
                except Exception as e:
                    print(e)
                    reply_msg = "error"
            elif func == "clear":
                try:
                    chatHistory.clear(line_id)
                    reply_msg = "對話紀錄已清除"
                    QuickReplyButtons.remove(QuickReplyButtons[0])
                except Exception as e:
                    print(e)
                    reply_msg = "error"
            else:
                reply_msg = "請輸入正確的指令"
        else:
            reply_msg = chat_llm(user_message, line_id)
        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text=reply_msg,
                quick_reply=QuickReply(
                    items=QuickReplyButtons
                )
            )
        )


def parseMessage(user_message):
    temp = user_message[1:].split(" ")
    func = temp[0]

    if len(temp) == 1:
        return func, ''
    
    args = temp[1]
    return func, args