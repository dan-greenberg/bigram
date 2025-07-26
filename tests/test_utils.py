from utils import pretty_print, remove_punctuation


def test_dict_outputs_as_expected():

    # Arrange
    test_input = {"key_1": 6, "key_2": 4, "key_3": 0, "key_4": 9}

    expected = '"key_1": 6\n"key_2": 4\n"key_3": 0\n"key_4": 9'

    # Act, assert
    assert pretty_print(test_input) == expected


def test_punctuation_remover_works():

    # Arrange, act, assert
    assert remove_punctuation("Sa.m?,!") == "Sam"
