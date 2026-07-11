def sentence_palindrome(sentence):

    output = []
    for char in sentence:
        if char.isalnum():
            output.append(char.lower())
    output = "".join(output)
    return output == output[::-1]

print(sentence_palindrome("Too hot to hoot."))
print(sentence_palindrome("Abc 012..##  10cbA"))