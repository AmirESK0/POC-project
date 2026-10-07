import random

words = ("aardvark", "albatross", "alligator", "antelope", "armadillo", "badger", "bat", "beaver", "bison", "boar", "buffalo", "camel", "caribou", "cheetah", "cougar", "coyote", "crab", "crow", "deer", "dolphin", "donkey", "duck", "eagle", "eel", "falcon", "ferret", "flamingo", "fox", "frog", "gecko", "giraffe", "goat", "goose", "hamster", "hedgehog", "horse", "hyena", "iguana", "jaguar", "jellyfish", "kangaroo", "koala", "lemur")
# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("**********")
    for x in hangman_art[wrong_guesses]:
        print(x)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for x in range(len(answer)):
                if answer[x] == guess:
                    hint[x] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("U WIN")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("U LOSE")
            is_running = False

if __name__ == "__main__":
    main()