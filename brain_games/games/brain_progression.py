import random


def make_data():
    first_number = random.randint(1, 10)
    step = random.randint(1, 10)
    return {"first_number": first_number, "step": step}


def get_first_number(data):
    return data["first_number"]


def get_step(data):
    return data["step"]


def make_progression(data):
    list = [get_first_number(data)]
    for _ in range(0, 10):
        list.append(list[-1] + get_step(data))
    return list


game_rules = 'What number is missing in the progression?\n'


def round():
    data = make_data()
    random_index = random.randrange(0, len(make_progression(data)))
    missed_element = str((make_progression(data))[random_index])
    new_list = make_progression(data)[:]
    new_list[random_index] = ".."
    string = ", ".join(str(x) for x in new_list)
    return string, missed_element
