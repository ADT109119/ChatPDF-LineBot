# Line PDF 問答機器人

這是一個使用 LangChain、FastAPI 和 Vue 構建的 Line Bot，可以透過 Line Liff 網頁上傳 PDF 文件並回答相關問題。

## 功能

- 上傳 PDF 文件
- 自然語言處理，從 PDF 中提取相關內容回答問題
- 使用 Line Bot 進行互動

## 技術

- **LangChain**: 用於構建問答系統和文本處理
- **FastAPI**: 用於構建 Web API 服務
- **Vue.js**: 用於構建用戶介面
- **Line Bot SDK**: 用於與 Line 平台集成

## 安裝(若想用 Docker 可跳過)

1. 複製存儲庫:
```
git clone https://github.com/your-repo/line-pdf-bot.git
```

2. 安裝伺服器依賴:
```
cd ChatPDF-LineBot
pip install -r requirements.txt
```
可考慮在虛擬環境中執行，這裡提供 Python 內建的虛擬環境指令:
```
cd ChatPDF-LineBot
python -m venv .\venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

3. 安裝 Node 依賴:
```
cd ChatPDF-LineBot/View
npn install
```

4. Build 前端網頁
```
cd View
npm install
npm run build
```

## 環境變數

伺服器或 Docker 可編輯環境變數

自己電腦上跑的話可複製 `.env.example` 文件，並改名為 `.env`，配置 API Key、模型等參數。

### 環境變量設定

| 變數 | 說明 | 預設值 |
|------|------|------|
| `MODEL_NAME` | 用於問答的模型名稱,多個模型以`\|`分隔 | `llama3-8b-8192\|gpt-3.5-turbo\|gpt-4-1106-preview` |
| `BASE_URL` | 對應模型的 API 基礎 URL,多個 URL 以`\|`分隔 | `https://api.groq.com/openai/v1\|https://api.openai.com/v1\|https://api.openai.com/v1` |
| `API_KEY` | 對應模型的 API 密鑰,多個密鑰以`\|`分隔 | `API_KEY_1\|API_KEY_2\|API_KEY_3` |
| `MAX_CHAT_HISTORY` | 保留的最大聊天記錄數 | `5` |
| `EMBEDDING_MODEL` | 用於文本嵌入的模型名稱(請填入HF模型路徑) | `sentence-transformers/all-MiniLM-L6-v2` |
| `EMBEDDING_DEVICE` | 運行文本嵌入模型的設備(cpu或cuda，可用cuda:0、cuda:1選擇顯卡) | `cpu` |
| `LINE_CHANNEL_ACCESS_TOKEN` | Line Bot 的access token | `YOUR_LINE_CHANNEL_ACCESS_TOKEN` |
| `LINE_CHANNEL_SECRET` | Line Bot 的secret | `YOUR_LINE_CHANNEL_SECRET` |
| `LINE_LIFF_ID` | Line LIFF 網頁 ID | `YOUR_LINE_LIFF_ID` |
| `FILE_MAX_SIZE` | 允許上傳的最大文件大小 | `5MB` |
| `SPACE_PER_USER` | 每個用戶可用的最大空間大小 | `200MB` |
| `ALLOW_FILE_TYPE` | 允許上傳的文件類型,多個類型以`,`分隔 | `pdf,csv,txt` |


## 運行

### 使用 Docker

```
docker run -d \
--name chatpdf-linebot \
-p 8000:8000 \
-e LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN \
-e LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET \
-e MODEL_NAME=YOUR_MODELS \
-e BASE_URL=BASE_URLS \
-e API_KEY=API_KEYS \
-e LINE_LIFF_ID=YOUR_LINE_LIFF_ID \
adt109119/chatpdf-linebot
```

### 本機直接運行

```
python .\main.py
```

## 貢獻

如果您有任何改進建議或錯誤修復，歡迎提交 Pull Request。

<a href="https://github.com/ADT109119/ChatPDF-LineBot/graphs/contributors" target="_blank">
  <img src="https://contrib.rocks/image?repo=ADT109119/ChatPDF-LineBot"/>
</a>


## License
This project is under the Apache 2.0 License. See [LICENSE](https://github.com/ADT109119/ChatPDF-LineBot/blob/main/LICENSE) for further details.

