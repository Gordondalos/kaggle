
def get_my_square(item):
    item = item + 3
    return item**2


def my_function(variable1, variable2):
    print(variable1)
    print(variable2)
    return get_my_square(variable2)


def print_word_by_letter(word):
    letters = []

    for letter in word:
        letters.append(letter)

    return letters


res = my_function('Коля', 3)
print(res)

result = print_word_by_letter('Привет как дела')
print(result)