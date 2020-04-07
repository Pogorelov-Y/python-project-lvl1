#!/usr/bin/env python


from brain_games.cli import say_your_name


introduction = 'Welcome to the Brain Games!\n'


def greeting(hello):
    print(hello)


def main():
    greeting(introduction)
    say_your_name()


if __name__ == '__main__':
    main()
