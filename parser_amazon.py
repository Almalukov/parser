from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Настройка параметров Chrome WebDriver для работы в headless-режиме
options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)

# URL страницы Amazon, которую нужно спарсить
url = "https://www.amazon.com/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A281407&ref=nav_em__nav_desktop_sa_intl_accessories_and_supplies_0_2_5_2"

# Открываем URL в веб-браузере
driver.get(url)

# Получаем HTML-код страницы
content = driver.page_source

# Инициализация объекта BeautifulSoup для парсинга HTML-кода
soup = BeautifulSoup(content, 'lxml')

# Поиск всех элементов продуктов на странице, с ограничением до 23 элементов
products = soup.find_all('div', {'class': 'sg-col-inner'}, limit=23)

# Создание пустого списка для хранения данных о продуктах
product_list = []

# Итерация по найденным продуктам
for product in products:
    # Извлечение элементов данных о продукте
    name_element = product.find('span', {'class': 'a-text-normal'})
    price_element = product.find('span', {'class': 'a-offscreen'})
    description_element = product.find('span', {'class': 'a-text-normal'})
    product_url_element = product.find('a', {'class': 'a-link-normal'})
    image_url_element = product.find('img', {'class': 's-image'})
    rating_element = product.find('span', {'class': 'a-icon-alt'})

    # Проверка наличия описания продукта
    if not description_element:
        continue

    # Извлечение данных о продукте и добавление их в список
    name = name_element.text if name_element else "N/A"
    price = price_element.text if price_element else "N/A"
    description = description_element.text
    product_url = product_url_element['href'] if product_url_element else "N/A"
    image_url = image_url_element['src'] if image_url_element else "N/A"
    rating = rating_element.text if rating_element else "N/A"

    # Добавление данных о продукте в список product_list
    product_list.append([name, price, description, rating, product_url, image_url])

# Создание DataFrame из данных о продуктах
df = pd.DataFrame(product_list, columns=['Name', 'Price', 'Description', 'Rating', 'Product_URL', 'Image_URL'])

# Запись данных в файл Excel
df.to_excel('products_amazon.xlsx', index=False)