#!/usr/bin/env python


from brain_games.cli import is_even, say_your_name
from brain_games.scripts.brain_games import greeting, introduction
import prompt
import random


game_rules = 'Answer "yes" if number even otherwise answer "no".\n'
count_attempts = 3


def logic_even_question(name, count_attempts=0):
    if count_attempts != 3:
        number = random.randint(1, 100)
        answer = prompt.string(f"Question: {number}\nYour answer: ")
        if is_even(number) == answer:
            print("Correct!")
            count_attempts += 1
            logic_even_question(name, count_attempts)
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{is_even(number)}'.
Let's try again, {name}!""")
    else:
        print(f"Congratulations, {name}!")


def main():
    greeting(introduction + game_rules)
    user_name = say_your_name()
    logic_even_question(user_name)


if __name__ == '__main__':
    main()
