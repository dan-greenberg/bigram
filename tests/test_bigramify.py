from bigramify import bigram


def test_bigram_of_blank_string_is_empty_dict():

    # Arrange, act, assert
    assert bigram("") == {}


def test_bigram_produces_correct_output():

    # Arrange
    test_input = (
        "I am Sam, Sam I am, I do like green eggs and ham. "
        "Sam is Sam, Sam I am, would you like green eggs and ham in a tree?"
    )

    expected = {
        "I am": 3,
        "am Sam": 1,
        "Sam Sam": 2,
        "Sam I": 2,
        "am I": 1,
        "I do": 1,
        "do like": 1,
        "like green": 2,
        "green eggs": 2,
        "eggs and": 2,
        "and ham": 2,
        "ham Sam": 1,
        "Sam is": 1,
        "is Sam": 1,
        "am would": 1,
        "would you": 1,
        "you like": 1,
        "ham in": 1,
        "in a": 1,
        "a tree": 1,
    }

    # Act, assert
    assert bigram(test_input) == expected
