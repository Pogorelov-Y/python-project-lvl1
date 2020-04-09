import random


def make_data():
    number1 = random.randint(1, 2)
    number2 = random.randint(1, 2)
    arithmetic_sign = random.choice(["+", "-", "*"])
    return {"number1": number1, "number2": number2, "arithmetic_sign": arithmetic_sign}


def make_number1(data):
    return data["number1"]


def make_number2(data):
    return data["number2"]


def make_arithmetic_sign(data):
    return data["arithmetic_sign"]


def calc_result(data):
    if make_arithmetic_sign(data) == "+":
        result = make_number1(data) + make_number2(data)
    elif make_arithmetic_sign(data) == "-":
        result = make_number1(data) - make_number2(data)
    else:
        result = make_number1(data) * make_number2(data)
    return str(result)


def question(data):
    return f"{make_number1(data)} {make_arithmetic_sign(data)} {make_number2(data)}"


def question_result(data):
    return calc_result(data)

game_rules = 'What is the result of the expression?\n'

def round():
    data = make_data()
    return question(data), question_result(data)
    
