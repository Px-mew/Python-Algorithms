"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true
"""

import requests
import json

numbers = [930, 997, 903, 905, 908, 974, 911, 912, 926, 980, 949, 982, 918, 990, 959]

for num in numbers:
    template = 'http://numbersapi.com/{}/math?json=true'
    res = requests.get(template.format(num))
    data_json = res.text
    data_again = json.loads(data_json)
    if data_again["found"]:
        print(num, "Interesting")
    else:
        print(num, "Boring")
