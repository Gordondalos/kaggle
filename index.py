# Переменные
a = 'строка'
b = 5
c = True  # False
d = 5.3

res = a + str(b)

list1 = ['Один', 'Два', 'Три', True]  # список = масиив - Изменяемый Массив, нумируется с нуля
lista = ['Oxana', 'cuñao', '26', 11, 'True']
# print(lista[0:])
lista[1] = 'blabla'
# print(lista)
# print(type(lista))

list1[0] = 123
list1[2] = 222
# print('list1', list1)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = [True, False, False]
lista1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
lista1[7] = 'Oxana'
# print(lista1)
x = list2 + lista1
# print(x)
# print(x[0::2])
# print(x[0::3])
# print(x[1::2])
# print(x[0:-1])
# print(x[::2])


list_sdf = ('Один1', 'Два1', 'Три1', 1)  # Кортеж не изменяемый массив
kortezh = ('Caracola', 11, '1979', 'lugar', 'precio')
# print(len(kortezh))
# print(kortezh[4])

# print(list1[0])
# print(list2[1])

print(len(list1))  # Выводит длину

# list1[-1] = False
# print(a[0:3]) # Срез списка / словаря / кортежа / строки
# print(list_sdf[0:2]) # Срез списка / словаря / кортежа
# print(list2[0:10:3]) # Срез списка / словаря / кортежа срез(от:до:шаг)

# Словари они же оbject
# 'Key': 'Value'
user = {
    'names': ['Вася', 'Maша', 'Коля'],
    'sex': 'M',
    'age': 18,
    'married': False,
    'cars': ('Один1', 'Два1', 'Три1', 1),
    'bio': {
        'asd': '123456',
        'names': ['Вася', 'Maша', 'Коля'],
    }
}

member = {
    'name': ['Clara', 'Ivan', 'unknown', 'Paul'],
    'status': ['beginner', 'profi', 'blanc'],
    'age': ['16', '23', '35', '40', '41', '52'],
    'Nationality': ['Austria', 'France', 'Russia', 'Spain'],
    'salary': ['cualif1', 'cualif2', 'cualif2'],
    'married': False,
    'times in Hac': [3, 6, 0, 0, ]
}

print(member)
# print(user['bio']['names'])
# print(user['married'])
#
# print(len(user))

user['smile'] = True
user['mayArr'] = list2
# print(user)
