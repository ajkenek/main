def parzyste(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

parzyste(range(10))