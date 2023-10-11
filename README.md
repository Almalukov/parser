# Amazon parser



![Amazon Logo](https://www.amazon.com/favicon.ico)

## Описание

Это небольшой проект для веб-парсинга данных с веб-сайта Amazon с использованием Selenium и BeautifulSoup. Скрипт позволяет извлекать информацию о продуктах с Amazon и сохранять результаты в формате Excel.

## Требования

- Python 3.10
- Docker

## Установка

1. Убедитесь, что у вас установлен Docker.

2. Склонируйте репозиторий с помощью команды:

   ```shell
   git clone https://git@github.com:Almalukov/parser.git

## Использование

1. В корне проекта создайте файл requirements.txt, если его нет, и добавьте следующие зависимости:

   ```shell
   beautifulsoup4
   pandas
   selenium

2. Создайте Docker образ, выполните следующую команду:

   ```shell
   docker build -t amazon_parser .
   
3. Запустите Docker контейнер:

   ```shell
   docker run amazon_parser

4. После завершения работы скрипта, результаты будут сохранены в файле
   products_amazon.xlsx

## Примечания
Если вам нужно использовать другой веб-браузер вместо Chrome, вы должны установить соответствующий WebDriver и обновить скрипт в parser_amazon.py для использования этого WebDriver.
Убедитесь, что версия ChromeDriver совместима с вашей версией браузера.
Пожалуйста, уважайте правила Amazon в отношении веб-скрапинга и не злоупотребляйте этим скриптом.
   






