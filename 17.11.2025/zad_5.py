def check(lista:list, liczba: int) -> bool:
    if liczba in lista:
        return True
    else:
        return False

print(check([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 3))