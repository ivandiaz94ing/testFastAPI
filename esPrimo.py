def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def esPrimo(numero):
    if numero < 2:
        return "False"
    for i in range(2, numero):
        if numero % i == 0:
            return "False"
    return "True"

