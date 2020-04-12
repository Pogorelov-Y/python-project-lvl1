import random


def make_number():
    """Make random natural numbers"""
    number = random.randint(1, 100)
    return number


def is_prime(number):
    """Return a simple number or not"""
    if number % 2 == 0:
        return number == 2
    i = 3
    while i * i <= number and number % i != 0:
        i += 2
    return i * i > number


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def round():
    """Form a question and answer string"""
    number = make_number()
    result_prime = "yes" if is_prime(number) else "no"
    return number, result_prime
