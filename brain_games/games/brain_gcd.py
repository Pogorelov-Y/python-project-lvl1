import random
from fractions import gcd


def make_data():
    """Make two random natural numbers"""
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    return {
        "number1": number1,
        "number2": number2,
    }


def get_number1(data):
    """Return random natural numbers"""
    return data["number1"]


def get_number2(data):
    """Return other random natural numbers"""
    return data["number2"]


def great_divisor(data):
    """Return the largest common divisor"""
    result = gcd(get_number1(data), get_number2(data))
    return str(result)


def question(data):
    """Form a string of two random numbers"""
    return "{} {}".format(get_number1(data),
                          get_number2(data))


GAME_RULES = 'Find the greatest common divisor of given numbers.\n'


def round():
    """Form a question and answer string"""
    data = make_data()
    return question(data), great_divisor(data)
