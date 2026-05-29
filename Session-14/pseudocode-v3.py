# TODO: Add Import statements (if needed)

# TODO: Define Constants
# set DEBUG true

# TODO: Define Variables

# TODO: FUNCTION Score Guess
# TODO:          accepts target_word and guess_word
def score_guess(target, guess):
    # TODO: Write score guess code
    score = [0] * 5
    
    print("Score guess code not ready")
    return score


# TODO: FUNCTION Read File Into Word List
def read_file_into_list():
    # TODO: write code to read file into list
    print("Read file into list code not ready")


# TODO: FUNCTION Display Greeting
def show_greeting():
    print("Welcome")


# TODO: FUNCTION Display Instructions
def show_instructions():
    print("Instructions")


# TODO: Any Optional Additional Functions

# TODO: FUNCTION Write get player name

# TODO: FUNCTION Write Ask player if they want instructions


# TODO: FUNCTION Play Game
def play_game():
    # TODO: Display Greeting

    # TODO Get player's name

    # TODO: Ask Player if they want instructions
    # TODO: Does Player Want Instructions?
    # TODO:     YES: Show instructions

    # TODO: Read target words into target word list
    # TODO: Read Allowed Words into Allowed word list

    # TODO: Set target word to a random word from target word list
    # TODO : Set guesses to 6

    # TODO: While NOT word correct AND if guesses NOT zero
    # TODO:      get Guess Word from user(allowed Word list
    # TODO:      score word
    # TODO:      Display score to player
    # TODO:      Guesses = guesses - 1

    # TODO: Display End of Game Message
    print("play the game code")


# TODO: FUNCTION Testing
def test_game():
    print("Testing game code")

    # -----------------------------------------------------------------

    # Test Case 1
    ## Arrange
    guess_word = "hello"
    target_word = "train"

    ## Act
    score = score_guess(guess_word, target_word)

    ## Assert
    print("Score:", score, "Expected:", [0, 0, 0, 0, 0])

    # -----------------------------------------------------------------


# TODO: Main Program
if DEBUG:
    test_game()
else:
    play_game()
