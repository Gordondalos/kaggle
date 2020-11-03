

a=(1,2,3,4,5,6,7,8,9,10,11,12)


# i = 0
# while len(a) > i:
#     print(a[i])
#     if i > 5:
#         break
#     i += 1
#
# print('Конец программы')

# i = 0
# while len(a) > i:
#     if i > 8:
#         break
#     if i == 4:
#         i += 3
#         continue
#
#     print(a[i])
#     i += 1
#
# print('Конец программы')

# for word in 'hello world':
#     print(word)

fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     # if x == "banana":
#     #     break
# else:
#     print("Finally finished!")

# a = [
#     {'b': ['a', 'b', 'c']},
#     {'c': 2, 'b': [1,2,3]},
#     {'b': ['banan', True, False]},
# ]
#
# for item in a:
#     for iter in item['b']:
#         print(iter)

# range (старт, стоп, шаг)
# for item in range(1,10,2):
#     print(item)

# for item in range(len(fruits)):
#     print(fruits[item])

for item in range(10):
    if item > 5:
        break
    print(item)
