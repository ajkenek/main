def parzysta(a: int) -> bool:
    if a % 2 == 0:
        return True
    else:
        return False

liczba = parzysta(3)

if liczba:
    print("Liczba parzysta")
else:
    print("Liczba nie parzysta")
