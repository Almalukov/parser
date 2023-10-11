# Используем официальный образ Python 3.10
FROM joyzoursky/python-chromedriver:3.9

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Устанавливаем необходимые библиотеки Python
RUN pip install --no-cache-dir pandas selenium beautifulsoup4 lxml openpyxl

# Копируем текущую директорию в рабочую директорию /app
COPY . /app


# Запускаем скрипт при старте контейнера
CMD ["python", "parser_amazon.py"]