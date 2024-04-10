# Import the functions to be tested
from project import is_valid, game_won, is_draw


def main():
    test_is_valid()
    test_game_won()
    test_is_draw()


# Define test cases
def test_is_valid():
    # Test valid positions
    assert is_valid("1", "|1|2|3|\n|4|5|6|\n|7|8|9|\n") == False
    assert is_valid("5", "|1|2|3|\n|4|5|6|\n|7|8|9|\n") == False
    assert is_valid("9", "|1|2|3|\n|4|5|6|\n|7|8|9|\n") == False

    # Test invalid positions
    assert is_valid("0", "|1|2|3|\n|4|5|6|\n|7|8|9|\n") == False
    assert is_valid("10", "|1|2|3|\n|4|5|6|\n|7|8|9|\n") == False
    assert is_valid("a", "|1|2|3|\n|4|5|6|\n|7|8|9|\n") == False


def test_game_won():
    # Test winning conditions
    assert game_won("|X|X|X|\n|4|5|6|\n|7|8|9|\n") == True
    assert game_won("|1|2|3|\n|X|X|X|\n|7|8|9|\n") == True
    assert game_won("|1|2|3|\n|4|5|6|\n|X|X|X|\n") == True
    assert game_won("|X|2|3|\n|X|5|6|\n|X|8|9|\n") == True
    assert game_won("|1|X|3|\n|4|X|6|\n|7|X|9|\n") == True
    assert game_won("|1|2|X|\n|4|5|X|\n|7|8|X|\n") == True
    assert game_won("|X|2|3|\n|4|X|6|\n|7|8|X|\n") == True
    assert game_won("|1|2|X|\n|4|X|6|\n|X|8|9|\n") == True
    assert game_won("|X|2|3|\n|4|X|6|\n|X|8|9|\n") == True
    assert game_won("|1|X|3|\n|4|X|6|\n|7|X|9|\n") == True
    assert game_won("|1|2|X|\n|4|5|X|\n|7|8|X|\n") == True
    assert game_won("|X|2|3|\n|X|5|6|\n|X|8|9|\n") == True
    assert game_won("|1|X|3|\n|X|5|6|\n|X|8|9|\n") == True
    assert game_won("|1|2|X|\n|X|5|6|\n|X|8|9|\n") == True
    assert game_won("|X|2|3|\n|4|X|6|\n|7|8|X|\n") == True
    assert game_won("|1|X|3|\n|4|X|6|\n|7|8|X|\n") == True
    assert game_won("|X|2|3|\n|4|5|X|\n|7|8|X|\n") == True
    assert game_won("|X|2|3|\n|4|5|6|\n|X|X|X|\n") == True
    assert game_won("|1|X|3|\n|4|X|6|\n|7|X|9|\n") == True
    assert game_won("|X|2|3|\n|X|5|6|\n|X|8|9|\n") == True
    assert game_won("|1|2|X|\n|4|5|X|\n|7|8|X|\n") == True


def test_is_draw():
    # Test draw condition
    assert is_draw("|X|O|X|\n|X|O|X|\n|O|X|O|\n") == False
    # Test not draw condition
    assert is_draw("|X|2|3|\n|4|O|6|\n|7|8|9|\n") == False
    assert is_draw("|X|2|O|\n|O|X|X|\n|X|O|X|\n") == False
    assert is_draw("|X|O|X|\n|X|O|X|\n|O|X|O|\n") == False


if __name__ == "__main__":
    main()
