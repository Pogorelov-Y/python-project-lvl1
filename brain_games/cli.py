import prompt


def say_your_name():
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name


def is_even(number):
    return "yes" if number % 2 == 0 else "no"
