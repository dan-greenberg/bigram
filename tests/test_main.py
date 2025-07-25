from main import bigram


def test_bigram_produces_correct_output():

    # Arrange
    test_input = ""
    expected = ""

    # Act, Assert
    assert bigram(test_input) == expected
