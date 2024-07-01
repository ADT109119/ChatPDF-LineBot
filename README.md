# Line PDF 問答機器人

這是一個使用 LangChain、FastAPI 和 Vue 構建的 Line Bot，可以透過 Line Liff 網頁上傳 PDF 文件並回答相關問題。

## 範例

| ![Screenshot_20240514-132200](https://github.com/ADT109119/ChatPDF-LineBot/assets/106337749/996fea6c-3ae8-4d9a-baff-7ada3860b4f9) | ![Screenshot_20240514-131836](https://github.com/ADT109119/ChatPDF-LineBot/assets/106337749/0cb06999-e8c3-4779-8fe2-c6f87a7a370c) |Demo 連結(每次更新時刪檔)  ![image](https://github.com/ADT109119/ChatPDF-LineBot/assets/106337749/c1860b26-3371-4b2d-935f-cc4823286092)   https://lin.ee/QajGJOY|
|------|------|------|

## 說明文件

* [中文](https://adt109119.github.io/ChatPDF-LineBot-Docs/)
* [English](https://adt109119.github.io/ChatPDF-LineBot-Docs/en/) (使用 ChatGPT 翻譯)

## 功能

目前支援以下幾種功能:
- [x] 上傳 PDF 文件
- [x] 自然語言處理，從 PDF 中提取相關內容回答問題
- [x] 自動 Embedding 文件
- [x] 使用 Line Bot 進行互動

尚待完成:
- [ ] 顯示用戶使用量
- [ ] 文件預覽
- [ ] 功能列表

## 技術

- **LangChain**: 用於構建問答系統和文本處理
- **FastAPI**: 用於構建 Web API 服務
- **Vue.js**: 用於構建用戶介面
- **Line Bot SDK**: 用於與 Line 平台集成

## Hugging Face 一鍵部署

本專案可以快速部署在 Hugging Face 上

支援 CloudFlare Tunnel 自訂網址

但要注意若無購買 Hugging Face 的永久儲存空間

每次更新或更改資料時檔案都匯遺失

[![](https://huggingface.co/datasets/huggingface/badges/resolve/main/deploy-on-spaces-lg-dark.svg)](https://huggingface.co/spaces/ADT109119/ChatPDF-LineBot?duplicate=true)

## 安裝
> 使用 Docker 的人可直接跳至第 5 步

### 1. 複製存儲庫:
```
git clone https://github.com/your-repo/line-pdf-bot.git
```

### 2. 安裝伺服器依賴:
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

### 3. 安裝 Node 依賴:
```
cd ChatPDF-LineBot/View
npn install
```

### 4. Build 前端網頁
```
cd View
npm install
npm run build
```

### 5. 登入 LINE 平台
   * 創建 Line Bot。
      * 新增一個提供者（Provider），例如「My Provider」。
      * 在「My Provider」新增一個類型為「Messaging API」的頻道（Channel），例如「My AI Assistant」。
      * 進到「My AI Assistant」頻道頁面，點選「Messaging API」頁籤，生成一個頻道的 channel access token。
   * 創建 LIFF 網頁。
      * 在與「Messaging API」同一個 `Provider` 內(例如:「My Provider」)新增一個類型為「Line Login」的頻道（Channel），例如「My LIFF Page」。
      * 進到「My LIFF Page」頻道頁面，點選「LIFF」頁籤，創建一個新的 LIFF 網頁。
      * `Endpoint URL` 填入 `https://<你的網域或IP地址>/liff`(可先隨便填後續再來改)。
      * `Scopes` 選項請勾選「chat_message.write」、「openid」。
      * 點選 `Add` 創建。

### 6. 登入 OpenAI、Groq 平台(或其他平台)
* 生成一個 OpenAI 的 API key。
* 也可以生成其他平台的API Key(例如 Groq)，只是該平台的 API 必須與 OpenAI 兼容，且要記得在下一步改`BASE_URL`

### 7. 設定環境變數

伺服器或 Docker 可直接設定環境變數

自己電腦上跑的話可複製 `.env.example` 文件，並改名為 `.env`，接著設定 API Key、模型等參數。

以下為 `環境變數列表` `*` 代表必改項目

#### 環境變數列表

| 變數 | 說明 | 預設值 |
|------|------|------|
| `MODEL_NAME` | 用於問答的模型名稱,多個模型以`\|`分隔 | `llama3-8b-8192\|gpt-3.5-turbo\|gpt-4-1106-preview` |
| `BASE_URL` | 對應模型的 API 基礎 URL,多個 URL 以`\|`分隔 | `https://api.groq.com/openai/v1\|https://api.openai.com/v1\|https://api.openai.com/v1` |
| * `API_KEY` | 對應模型的 API 密鑰,多個密鑰以`\|`分隔 | `API_KEY_1\|API_KEY_2\|API_KEY_3` |
| `MAX_CHAT_HISTORY` | 保留的最大聊天記錄數 | `5` |
| `EMBEDDING_MODEL` | 用於文本嵌入的模型名稱(請填入HF模型路徑) | `sentence-transformers/all-MiniLM-L6-v2` |
| `EMBEDDING_DEVICE` | 運行文本嵌入模型的設備(cpu或cuda，可用cuda:0、cuda:1選擇顯卡) | `cpu` |
| * `LINE_CHANNEL_ACCESS_TOKEN` | Line Bot 的access token | `YOUR_LINE_CHANNEL_ACCESS_TOKEN` |
| * `LINE_CHANNEL_SECRET` | Line Bot 的secret | `YOUR_LINE_CHANNEL_SECRET` |
| * `LINE_LIFF_ID` | Line LIFF 網頁 ID | `YOUR_LINE_LIFF_ID` |
| * `LINE_LOGIN_CHANNEL_ID` | Line LIFF 所在的 LINE Login Channel ID | `YOUR_LINE_LOGIN_CHANNEL_ID` |
| `FILE_MAX_SIZE` | 允許上傳的最大文件大小 | `5MB` |
| `SPACE_PER_USER` | 每個用戶可用的最大空間大小 | `200MB` |
| `ALLOW_FILE_TYPE` | 允許上傳的文件類型,多個類型以`,`分隔 | `pdf,csv,txt` |


### 8. 運行伺服器

#### 使用 Docker

![Docker Image Size (tag)](https://img.shields.io/docker/image-size/adt109119/chatpdf-linebot/latest)

```
docker run -d \
--name chatpdf-linebot \
-p 8000:8000 \
-v /local/file/store/path:/app/db
-e LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN \
-e LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET \
-e LINE_LIFF_ID=YOUR_LINE_LIFF_ID \
-e LINE_LOGIN_CHANNEL_ID=YOUR_LINE_LOGIN_CHANNEL_ID \
-e MODEL_NAME=YOUR_MODELS \
-e BASE_URL=BASE_URLS \
-e API_KEY=API_KEYS \
adt109119/chatpdf-linebot
```

#### 本機直接運行

若 1. ~ 4. 步的安裝接無問題，僅需直接執行一以下指令便可開啟伺服器

預設使用 `PORT` `8000`
```
python .\main.py
```

### 9. 回到 LINE 設定
* Line Bot 設定
  * 進到「My AI Assistant」頻道頁面，點選「Messaging API」頁籤，設置「Webhook URL」，填入應用程式網址並加上「/callback」路徑，例如 `https://line.the-walking.fish.com/callback`，點選「Update」按鈕。
  * 點選「Verify」按鈕，驗證是否呼叫成功。
  * 將「Use webhook」功能開啟。
  * 將「Auto-reply messages」功能關閉。
  * 將「Greeting messages」功能關閉。
  
* Line LIFF 網頁設定
  * 進到「LIFF」頁籤
  * 若原本`Endpoint URL` 隨便填的，現在請正式填入 LIFF 網頁網址，路徑為「/liff」，例如 `https://line.the-walking.fish.com/liff`。
  * 回到「LIFF」頁籤，複製「LIFF URL」
 
* 圖文選單設定
  * 進到「LINE Official Account Manager」
  * 在側邊欄找到「圖文選單」
  * 點選「建立」
  * 名稱、版型等可照自己的喜好填寫
  * 在「動作」選擇「連結」，並填入上一部複製的 LIFF URL
  * 按「儲存」

## 貢獻

如果您有任何改進建議或錯誤修復，歡迎提交 Pull Request。

<a href="https://github.com/ADT109119/ChatPDF-LineBot/graphs/contributors" target="_blank">
  <img src="https://contrib.rocks/image?repo=ADT109119/ChatPDF-LineBot"/>
</a>

## 聯繫作者

你可以透過以下方式與我聯絡

- 2.jerry32262686@gmail.com


## License
This project is under the Apache 2.0 License. See [LICENSE](https://github.com/ADT109119/ChatPDF-LineBot/blob/main/LICENSE) for further details.

