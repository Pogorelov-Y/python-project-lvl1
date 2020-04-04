#!/usr/bin/env python


from brain_games.cli import say_your_name


def greeting(hello):
    print(hello)


def main():
    greeting('Welcome to the Brain Games!')
    say_your_name()


if __name__ == '__main__':
    main()
