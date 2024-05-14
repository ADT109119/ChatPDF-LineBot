# Dockerfile
FROM python:3.10.12

## Set working directory
WORKDIR /app

## Set the timezone
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy files
COPY . .

# Install Python requirements
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs npm &&\
    cd View &&\
    npm install -y &&\
    npm run build &&\
    cd .. &&\
    cp .env.example .env &&\
    pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]
