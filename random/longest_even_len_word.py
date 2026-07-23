import string
# Longest Even Length Word:
# Write a function to return the longest even length word in a sentence. 

sample_input = "Be not afraid of greatness, some are born great, some achieve greatness, and some have greatness thrust upon them."

def longest_even_length_word(sentence):
    max_len = 0
    length = 0

    for char in sentence:
        if char.isalpha():
            length += 1
        elif length % 2 == 0:
            max_len = max(max_len, length)
            length = 0
        else:
            length = 0
    
    return max_len

max_len = longest_even_length_word(sample_input)
print(max_len)


def longest_even_length_word_2(sentence):
    longest_word = ""

    for word in sentence.split():

        word = word.strip(string.punctuation)

        if len(word) % 2 == 0 and len(word) > len(longest_word):
            longest_word = word

    return longest_word


sample_input = "Be not afraid of greatness, some are born great, some achieve greatness, and some have greatness thrust upon them."

print(longest_even_length_word_2(sample_input))