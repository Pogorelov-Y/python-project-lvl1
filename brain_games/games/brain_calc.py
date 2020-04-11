import random


def make_data():
    """Make two random natural numbers and an arithmetic sign"""
    number1 = random.randint(1, 2)
    number2 = random.randint(1, 2)
    arithmetic_sign = random.choice(["+", "-", "*"])
    return {
        "number1": number1,
        "number2": number2,
        "arithmetic_sign": arithmetic_sign
    }


def get_number1(data):
    """Return random natural numbers"""
    return data["number1"]


def get_number2(data):
    """Return other random natural numbers"""
    return data["number2"]


def get_arithmetic_sign(data):
    """Return random arithmetic_sign"""
    return data["arithmetic_sign"]


def calc_result(data):
    """Return the result of a mathematical operation on two random numbers"""
    if get_arithmetic_sign(data) == "+":
        result = get_number1(data) + get_number2(data)
    elif get_arithmetic_sign(data) == "-":
        result = get_number1(data) - get_number2(data)
    else:
        result = get_number1(data) * get_number2(data)
    return str(result)


def question(data):
    """Form a string of two random numbers and an arithmetic sign"""
    return " {} {} {}".format(get_number1(data),
                              get_arithmetic_sign(data),
                              get_number2(data))


game_rules = 'What is the result of the expression?\n'


def round():
    """Form a question and answer string"""
    data = make_data()
    return question(data), calc_result(data)
