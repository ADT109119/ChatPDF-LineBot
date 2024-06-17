# 使用 Node.js 來構建 Vue.js 網頁
FROM node:16 AS build

# 設置工作目錄
WORKDIR /app

# 複製前端代碼
COPY View ./View

# 進入前端目錄並安裝依賴和構建
WORKDIR /app/View
RUN npm install && npm run build

# 使用 Python 作為基礎映像
FROM python:3.10.12-slim

# 設置工作目錄
WORKDIR /app

# 設置時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 設置 IN_DOCKER 環境變量
ENV IN_DOCKER=1

# 複製後端代碼和構建後的前端文件
COPY . .
COPY --from=build /app/View/dist /app/View/dist

# Install Python requirements
RUN ls && \
    cp .env.example .env && \
    pip install --no-cache-dir -r reurements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]
