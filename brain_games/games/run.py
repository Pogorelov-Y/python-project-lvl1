import prompt


def run(games):
    """Play the game with question and answer string"""
    print("Welcome to the Brain Games!")
    print(games.game_rules)
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    attempts = 3
    while attempts:
        question, question_result = games.round()
        answer = prompt.string(f"Question: {question}\nYour answer: ")
        if answer == question_result:
            print("Correct")
            attempts -= 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  .format(answer, question_result))
            print(f"Let's try again, {name}!")
            break
    if attempts == 0:
        print(f"Congratulations, {name}!")
