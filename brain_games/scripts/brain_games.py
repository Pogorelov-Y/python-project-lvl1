#!/usr/bin/env python


import prompt


def hello():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


def main():
    hello ()


if __name__ == '__main__':
    main()
