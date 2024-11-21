FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN ls -la /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN sed -i 's/\r$//' build_test.txt

RUN chmod +x ./build_test.txt

CMD ["bash", "./build_test.txt"]