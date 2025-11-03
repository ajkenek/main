def mnozenie(lista):
    wynik = []
    for n in lista:
        wynik.append(n * 2)
    return wynik


print(mnozenie([1,2,3,8,9]))


def mnozenie_fast(list):
    return [num * 2 for num in list ]

print(mnozenie_fast([6,9,13,14,51]))