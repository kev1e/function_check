def remove_palindroms(list_):
    word = 0
    while word < len(list_):
        x = str(list_[word]).lower().split()
        element_list = "".join(x)
        if element_list == element_list[::-1]:
            list_.pop(word)
        else:
            word += 1
