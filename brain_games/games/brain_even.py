import random


GAME_RULES = 'Answer "yes" if number even otherwise answer "no".\n'


def round():
    """Make random natural numbers to determine its parity"""
    number = random.randint(1, 100)
    question_result = "yes" if number % 2 == 0 else "no"
    return number, question_result
