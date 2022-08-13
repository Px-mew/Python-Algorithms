def numerics(n):
    """
    Напишите функцию numerics(n), принимающую на вход 1 натуральное 4х значное число, а возвращающую список цифр из которых состоит число.
    """
    return [int(i) for i in list(str(n))]

def kaprekar_step(L):
    """
    Напишите функцию kaprekar_step(L), принимающую на вход список натуральных чисел (цифр из которых состоит число, проходящее через процесс Капрекара), проводит 1 шаг сходимости к постоянной Капрекара и возвращает 4х значное число.
    """
    L.sort()
    a = ''.join([str(i) for i in L])
    b = a[::-1]
    return int(b) - int(a)

def kaprekar_loop(n):
    """
    Напишите функцию kaprekar_loop(n), которая принимает целое 4х значное число (больше 1000, содержащее хотя бы 2 разные цифры), и запускающую "Процесс Капрекара", выводящую на печать каждое число цикла с новой строки до тех пор, пока не будет получено число 6174 (каждое, включая 6174).
    """
    if not kaprekar_check(n):
        return 
    kaprekar_list = []
    while n != 495 and n != 6174 and n != 549945 and n != 631764 :
        print(n)
        n = kaprekar_step(numerics(n))
        if n in kaprekar_list:
            print(f"Следующее число - {n}, кажется процесс зациклился...")
            return
        kaprekar_list.append(n)
    print(n)    

def kaprekar_check(n):
    """
    Напишите функцию kaprekar_check(n), принимающую на вход 1 натуральное число, а возвращающую логическое значение (True или False) в зависимости от предварительной проверки на возможность прохождения Процесса Капрекара для него.
    """
    if n == 1000 or n == 100 or n == 100000:
        print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")
        return False
    if len([int(i) for i in list(str(n))]) < 3 or len([int(i) for i in list(str(n))]) > 6 or len([int(i) for i in list(str(n))]) == 5:
        print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")
        return False
    if  len(set([int(i) for i in list(str(n))])) == 1:
        print(f"Ошибка! На вход подано число {n} - все цифры одинаковые")
        return False
    return True

def convert(num, to_base=10, from_base=10):
    """
    Напишите функцию convert(num, to_base=10, from_base=10), переводящую число из одной системы счисления в другую
    """
    if from_base == to_base:
        return num

    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if from_base != 10:
        r = len(str(num))-1
        res = 0
        for c in str(num).upper():
            res += alphabet.find(c)*from_base**r
            r -= 1
        num = int(res)

    if to_base == 10:
        return str(num)

    list_ost = []
    num = int(num)

    while num >= to_base:
        ost = num % to_base
        num //=  to_base
        list_ost.append(alphabet[ost])
    list_ost.append(alphabet[num])
    return ''.join(list_ost[::-1])
    
def kaprekar(n, base=10):
    """
    Напишите функцию kaprekar(n, base=10), принимающую на вход натуральное число (int для десятичной системы счисления, либо строку для иной) и основание системы счисления, а возвращающую:

    True, если число является Числом Капрекара
    False, если число НЕ является Числом Капрекара
    По умолчанию функция считает, что передаваемое число в десятичной системе счисления.
    """
    n = convert(n, 10, base)
    n = int(n)
    n2 = str(n * n)
    n2 = convert(n2, base, 10)
    n2 = str(n2)
    for i in range(1, len(n2)):
        m1 = convert(n2[:i], 10, base)
        m2 = convert(n2[i:], 10, base)
        if int(m1)+int(m2) == n and int(m2) != 0:
            return(True)
    return(False)
    

print(kaprekar(10))


test_1 = [9, 45, 55, '99', '297', 703, 999, '2223', 2728, '4879']
test_2 = [10, 46, 56, 100, 298, 704, '1000', '2224', '2729', '4880']
test_3 = ['6', 'A', 'F', '33', '55', '5B', '78', '88', 'AB', 'CD', 'FF', '15F', '334', '38E']

print([kaprekar(i) for i in test_1]) # Тест чисел Капрекара из системы с основанием 10

print([kaprekar(i) for i in test_2 ]) # Тест НЕ чисел Капрекара из системы с основанием 10

print([kaprekar(i, base=16) for i in test_3]) #Тест чисел Капрекара из системы с основанием 16
