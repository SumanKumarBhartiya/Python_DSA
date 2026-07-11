def reverse_words_in_a_string(s):

    l_data = s.split(" ")
    ans = ""
    print(l_data)
    for w in l_data:
        if w != "":
            ans = " " + w.strip() + ans

    return ans.strip()


# print(reverse_words_in_a_string("the sky is blue"))
# print(reverse_words_in_a_string("hello world"))
print(reverse_words_in_a_string("a good       example"))
