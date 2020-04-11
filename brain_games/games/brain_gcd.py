import random
from fractions import gcd


def make_data():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    return {
        "number1": number1,
        "number2": number2,
    }


def get_number1(data):
    return data["number1"]


def get_number2(data):
    return data["number2"]


def great_divisor(data):
    result = gcd(get_number1(data), get_number2(data))
    return str(result)


def question(data):
    return "{} {}".format(get_number1(data),
                          get_number2(data))


game_rules = 'Find the greatest common divisor of given numbers.\n'


def round():
    data = make_data()
    return question(data), great_divisor(data)
