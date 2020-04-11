import random


def make_number():
    number = random.randint(1, 100)
    return number


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    i = 3
    while i * i <= number and number % i != 0:
        i += 2
    return i * i > number


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def round():
    number = make_number()
    result_prime = "yes" if is_prime(number) else "no"
    return number, result_prime
