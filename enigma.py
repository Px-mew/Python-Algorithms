def cipher(symbol, n):
    """
        Функция получает в качестве аргумента символ и шаг сдвига (n).
        Возвращает символ, который находится на n правее исходного символа в алфавите.
    """
    code_symbol = ord(symbol)
    if ord('A') <= code_symbol <= ord('Z'):
        if code_symbol + n > ord('Z'):
            code_symbol = code_symbol + n - 26
        elif code_symbol + n < ord('A'):
            code_symbol = code_symbol + n + 26
        else:
            code_symbol = code_symbol + n
    symbol = chr(code_symbol)
    return symbol

def rotor(enig, symbol, n, reverse=False):
    if reverse:
        code = enig[n].find(symbol)
        return enig[0][code]
    else:
        code = enig[0].find(symbol)
        return enig[n][code]
    
def reflector(symbol, n):
    enig = [('A','Y'), ('B','R'), ('C','U'), ('D','H'), ('E','Q'), ('F','S'), ('G','L'), ('I','P'), ('J','X'), ('K','N'), ('M','O'), ('T','Z'), ('V','W')]
    if n == 0:
        return symbol
    for i in enig:
        if i[0] == symbol:
            return i[1]
    for i in enig:
        if i[1] == symbol:
            return i[0]

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    #your code
    text = [c for c in text.upper() if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    text_cipher = ''
    classic = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
        'AJDKSIRUXBLHWTMCQGZNPYFVOE',
        'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        ]

    enig = [classic[0], classic[rot1], classic[rot2], classic[rot3]]
    enig[rot1]=enig[rot1][shift1:]+enig[rot1][:shift1]
    enig[rot2]=enig[rot2][shift2:]+enig[rot2][:shift2]
    enig[rot3]=enig[rot3][shift3:]+enig[rot3][:shift3]
    print(enig)
   
    for c in text:
            
        print(c)
        print(enig[1])
        print(enig[2])
        print(enig[rot3])
    
        c = rotor(enig, c, rot3)
        print(c)
        c = rotor(enig, c, rot2)
        print(c)
        c = rotor(enig, c, rot1)
        print(c)
        c = reflector(c, ref)
        print(c)
        c = rotor(enig, c, rot1, reverse=True)
        print(c)
        c = rotor(enig, c, rot2, reverse=True)
        print(c)
        c = rotor(enig, c, rot3, reverse=True)
        print(c)
        text_cipher += c
    return text_cipher

print(enigma('BDZGOWC', 1, 1, 0, 2, 0, 3, 0))

