def add(*steves):
    sum = 0
    for number in steves:
        sum += number
    return sum


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)
