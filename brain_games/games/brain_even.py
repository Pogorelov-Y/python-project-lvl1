import random


def round():
    number = random.randint(1, 2)
    question_result = "yes" if number % 2 == 0 else "no"
    return number, question_result
