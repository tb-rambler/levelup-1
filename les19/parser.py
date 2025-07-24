from bs4 import BeautifulSoup

import requests

# url = "https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F"

# headers = {}
# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.find('h1', {'id': "firstHeading"}).get_text())


url = "https://lenta.ru/"
page = requests.get(url)
# print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
all_news = soup.find_all('div', class_ = 'card-mini__text')
filtered = []
for data in all_news:
    if data.find("div") is not None:
        filtered.append(data.text)
for data in filtered:
    print(data[:-5])
