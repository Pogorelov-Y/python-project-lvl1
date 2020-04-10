import random


def make_data():
    number1 = random.randint(1, 2)
    number2 = random.randint(1, 2)
    arithmetic_sign = random.choice(["+", "-", "*"])
    return {
        "number1": number1,
        "number2": number2,
        "arithmetic_sign": arithmetic_sign
    }


def get_number1(data):
    return data["number1"]


def get_number2(data):
    return data["number2"]


def get_arithmetic_sign(data):
    return data["arithmetic_sign"]


def calc_result(data):
    if get_arithmetic_sign(data) == "+":
        result = get_number1(data) + get_number2(data)
    elif get_arithmetic_sign(data) == "-":
        result = get_number1(data) - get_number2(data)
    else:
        result = get_number1(data) * get_number2(data)
    return str(result)


def question(data):
    return " {} {} {}".format(get_number1(data),
                              get_arithmetic_sign(data),
                              get_number2(data))


game_rules = 'What is the result of the expression?\n'


def round():
    data = make_data()
    return question(data), calc_result(data)
