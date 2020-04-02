import prompt


def say_your_name():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

