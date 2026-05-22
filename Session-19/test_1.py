DEBUG = True

secret = "HELLO"
guess = "ALLOW"

def score_guess(target, guess):
    result = [0] * 5
    secret_letters = list(target)

    for i in range(5):
        if guess[i] == secret_letters[i]:
            result[i] = 2
            secret_letters[i] = "_"

    for i in range(5):
        for j in range(5):
            if guess[i] == secret_letters[j]:
                result[i] = 1
                secret_letters[j] = "_"

    return result


def test_game():
    print("Testing game code...")

    # ---------------------------------------------
    print("Test Case 1: Score word, all 0s")
    ## Arrange
    guess_word = "games"
    target_word = "potty"
    ## Act
    score = score_guess(target_word, guess_word)
    ## Assert
    print(f"Target: {target_word} | Guess: {guess_word} | Score: {score} | Expected: [0, 0, 0, 0, 0]")


if DEBUG:
    test_game()