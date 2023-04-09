# Использование официального образа Python 3
FROM python:3

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование файла pyth.py внутрь контейнера
COPY pyth.py /app
COPY requirements.txt /app
COPY Dockerfile.dockerfile /app

# Установка зависимостей через pip
RUN pip install --no-cache-dir -r requirements.txt

# Определение команды, которая будет запущена при старте контейнера
CMD ["python", "pyth.py"]