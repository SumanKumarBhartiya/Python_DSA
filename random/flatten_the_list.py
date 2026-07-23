output = []
def flatten_the_list(data):

    for val in data:
        if type(val) is list:
            flatten_the_list(val)
        else:
            output.append(val)

flatten_the_list([1,[2,3, [4, [5, 6]]]])

print(output)
            


