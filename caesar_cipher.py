"""
    ШИФР ЦЕЗАРЯ
    программа способна шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
"""


def cipher(symbol, n):
    """
        Функция получает в качестве аргумента символ и шаг сдвига (n).
        Возвращает символ, который находится на n правее исходного символа в алфавите.
    """
    # делаем буквы строчными
    f = False
    if symbol.isupper():
        f = True
        symbol = symbol.lower()
    # получаем код символа
    code_simbol = ord(symbol)
    # сдвиг для английских букв
    if ord('a') <= code_simbol <= ord('z'):
        if code_simbol + n > ord('z'):
            code_simbol = code_simbol + n - 26
        elif code_simbol + n < ord('a'):
            code_simbol = code_simbol + n + 26
        else:
            code_simbol = code_simbol + n
    # сдвиг для русских букв
    if ord('а') <= code_simbol <= ord('я'):
        if code_simbol + n > ord('я'):
            code_simbol = code_simbol + n - 32
        elif code_simbol + n < ord('а'):
            code_simbol = code_simbol + n + 32
        else:
            code_simbol = code_simbol + n
    # возвращаем символ по коду, и регистр
    symbol = chr(code_simbol)
    if f:
        symbol = symbol.upper()
    return(symbol)


line = input('Введите строку: ')
process_line = ''
n = int(input('шаг сдвига: '))

#for n in range(26):
for symbol in list(line):
    if symbol.isalpha():
        process_line = process_line + cipher(symbol, n)
    else:
        process_line = process_line + symbol

print(process_line)
