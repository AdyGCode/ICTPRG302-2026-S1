import random

# DEBUG = True
DEBUG = False


def score_guess(guess_word, target_word):
    # Create a NEW score list
    score = []

    for letter in range(len(guess_word)):

        # Correct letter in correct spot
        if guess_word[letter] == target_word[letter]:
            score.append(2)

        # Correct letter but wrong spot
        elif guess_word[letter] in target_word:
            score.append(1)

        # Letter not in word
        else:
            score.append(0)

    return score


def display_score(score, guess_word):
    # Display score symbols
    for value in score:

        if value == 0:
            print("-", end=" ")

        elif value == 1:
            print("?", end=" ")

        elif value == 2:
            print("O", end=" ")

    print()

    # Display guess word letters
    for letter in guess_word:
        print(letter.upper(), end=" ")

    print()


def read_words_from_file(words):
    word_list = []

    file = open(words)

    for line in file:
        print(line)
        word_list.append(line.strip())

    file.close()

    return word_list


def random_word(word_list):  # Accept word_list as an argument

    return random.choice(word_list)


def test_game():
    print()
    print(" Test: Guess Vs Target")

    guess_word = "score"
    target_word = "guess"

    score = score_guess(guess_word, target_word)

    print(" Score: ", score, "Expected:", [1, 0, 0, 0, 1])

    # Arrange
    words = "words.txt"

    # Act
    words_list = read_words_from_file(words)

    for count in range(3):
        random_target = random_word(words_list)

        print(random_target)


def play_game():
    target_word = "hello"

    print("---- Playing The Game ----")

    # set guess attempts to 6
    attempts = 6

    guess_word = input("Enter a 5-letter word: ")

    # while attemnpts not zero, and guess word not equal to target word:
    while attempts != 0 and guess_word != target_word:
        # score the guess
        score = score_guess(guess_word, target_word)
        # display the score to the player
        display_score(score, guess_word)
        # if target word not equal to guess word:

        # get guess word from user

        # subtract 1 from attempts

        # end of if
    # end of while


def show_greeting():
    print("** Welcome to my Wordle game **")


def show_instructions():
    print()
    print("Can you guess the 5 letter word in 6 goes or less?")
    print()
    print("0 = GREY")
    print("1 = YELLOW")
    print("2 = GREEN")
    print()


if DEBUG == True:
    test_game()
else:
    play_game()