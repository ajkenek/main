def lista(first: list, second: list) -> list:
    return [i ** 3 for i in set(first + second)]

print(lista([1,2,3],[4,5,6]))