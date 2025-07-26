from utils import remove_punctuation


# put text into a bigram dictionary
def bigram(input_text):

    running_bigram = {}

    # split the sentence
    words = input_text.split()

    for i, word in enumerate(words):
        # if it's not the last word
        if i < len(words) - 1:
            # remove punctuation
            bigram_key = f"{remove_punctuation(word)} {remove_punctuation(words[i+1])}"
            # if the bigram has appeared before, increment the count
            # otherwise, add it to the dictionary
            if bigram_key in running_bigram:
                running_bigram[bigram_key] += 1
            else:
                running_bigram[bigram_key] = 1

    return running_bigram
