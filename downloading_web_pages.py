"""
Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python. В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего.
"""

from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
list_text = {}
max = 0

while "<code>" in s:
    if s[s.find("<code>")+6:s.find("</code>")] in list_text:
        list_text[s[s.find("<code>")+6:s.find("</code>")]] += 1
    else:
        list_text[s[s.find("<code>")+6:s.find("</code>")]] = 1
    if max <= list_text[s[s.find("<code>")+6:s.find("</code>")]]:
        max = list_text[s[s.find("<code>")+6:s.find("</code>")]]
    s = s[s.find("</code>")+7::]

for key in list_text:
    if list_text[key] == max:
        print(key)
