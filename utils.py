import string


# print a dictionary in the format
# if dictionary looks like {"key_1": 4, "key_2": 3, "key_3": 0}
# print as:
# "key_1": 4
# "key_2": 3
# "key_3": 0
def pretty_print(input_dict):

    pretty = ""

    printer = list(input_dict.items())

    if printer:
        # print the first key/value pair to avoid an unwanted newline
        k, v = printer[0]
        pretty = f'"{k}": {v}'
        # for all the rest, print a newline and the next pair
        for k, v in printer[1:]:
            pretty = f'{pretty}\n"{k}": {v}'

    return pretty


# remove punctuation from a word
def remove_punctuation(word):
    return word.translate(str.maketrans("", "", string.punctuation))
