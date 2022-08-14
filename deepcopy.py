def list_pull(L, res):
    """
    Не используя метод deepcopy скопируйте всё содержимое списка L1 в L2.
    """
    res = L[:]
    for i in range(len(L)):
        if type(L[i]) == list:
            res[i] = list_pull(L[i], res[i])[:]
    return res

L1 = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]
L2 = list_pull(L1, [])

print(L2)