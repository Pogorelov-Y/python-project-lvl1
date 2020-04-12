import random


def make_data():
    """Make two random natural numbers: first_number and step"""
    first_number = random.randint(1, 10)
    step = random.randint(1, 10)
    return {"first_number": first_number, "step": step}


def get_first_number(data):
    """Return random natural numbers"""
    return data["first_number"]


def get_step(data):
    """Return step: random natural numbers"""
    return data["step"]


def make_progression(data):
    """Return a list of 10 elements"""
    list = [get_first_number(data)]
    for _ in range(0, 10):
        list.append(list[-1] + get_step(data))
    return list


GAME_RULES = 'What number is missing in the progression?\n'


def round():
    """Form a question and answer string"""
    data = make_data()
    random_index = random.randrange(0, len(make_progression(data)))
    missed_element = str((make_progression(data))[random_index])
    new_list = make_progression(data)[:]
    new_list[random_index] = ".."
    string = ", ".join(str(x) for x in new_list)
    return string, missed_element
