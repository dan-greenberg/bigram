import sys

from main import main


def test_main_with_blank_produces_blank(monkeypatch, capsys):

    # Arrange
    monkeypatch.setattr(sys, "argv", ["main.py", ""])

    # Act
    main()

    # Assert
    assert capsys.readouterr().out.strip() == ""


def test_main_produces_correct_output(monkeypatch, capsys):

    # Arrange
    test_input = (
        "I am Sam, Sam I am, I do like green eggs and ham. "
        "Sam is Sam, Sam I am, would you like green eggs and ham in a tree?"
    )

    expected = (
        '"i am": 3\n"am sam": 1\n"sam sam": 2\n"sam i": 2\n"am i": 1\n'
        '"i do": 1\n"do like": 1\n"like green": 2\n"green eggs": 2\n"eggs and": 2\n'
        '"and ham": 2\n"ham sam": 1\n"sam is": 1\n"is sam": 1\n"am would": 1\n'
        '"would you": 1\n"you like": 1\n"ham in": 1\n"in a": 1\n"a tree": 1'
    )
    monkeypatch.setattr(sys, "argv", ["main.py", test_input])

    # Act
    main()

    # Assert
    assert capsys.readouterr().out.strip() == expected
