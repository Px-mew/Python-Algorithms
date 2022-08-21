"""
В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица. Просуммируйте все числа в ней. Для доступа к ячейкам используйте возможности BeautifulSoup.
"""

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
sum = 0
for tag in soup.find_all('td'):
    sum += int(tag.string)
print('Сумма -', sum)
