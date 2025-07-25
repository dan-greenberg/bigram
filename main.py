import sys


def bigram(input):
    return input


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input>")
        sys.exit(1)

    print(bigram(sys.argv[1]))


if __name__ == "__main__":
    main()
