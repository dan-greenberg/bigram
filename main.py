import sys

from bigramify import bigram
from utils import pretty_print


# handle improper number of args
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input>")
        sys.exit(1)

    # get the bigrams and then pretty print the dictionary
    print(pretty_print(bigram(sys.argv[1])))


if __name__ == "__main__":
    main()
