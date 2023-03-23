# lambda, exception
# lambda arguments: expression
# filter, map

# try:
#     code
# except:
#     message
#     code
# finally:
#     messsage
#      code

# name = 'kun aguero'
# print(name)
# name = name.split()
# print(name)


# players = []

# while True:
#     print(players)
#     try:
#         data = input('enter fullname: Leo Messi 10 ').split()
#         players.append({f'{data[0]} {data[1]}': data[2]})
#         # index = int(input('enter index: 0) name 1) surname 2) number'))
#         index = input('enter index: (0 1 2)').split()
#         if len(index) == 1:
#             print(data[int(index[0])])
#         elif len(index) == 2:
#             print(data[int(index[0])], data[int(index[1])])
#         elif len(index) == 3:
#             print(data[int(index[0])], data[int(
#                 index[1])], data[int(index[2])])
#         else:
#             print('index out of range!')

#     except:
#         print('only integer! wrong index!')

#     # except ValueError:
#     print('only integer!')
# except IndexError:
#     print('wrong index!')


# try:
#     print(int('34'))
# except:
#     print('error!')
# finally:
#     print('checked!')


# print(23 + 'dsfs')
# print(name)
# print('123'[4])


# numbers = list(range(1, 11))
#
# mapped_numbers = list(map(lambda n: n + 20, numbers))
# print(numbers)
# print(mapped_numbers)


# filtered_nums = list(filter(lambda n: n % 2 == 0, numbers))
# print(numbers)
# print(filtered_nums)


# lambda_func = lambda *args: sum(args)
# print(lambda_func(2, 3, 4))

# def plus(a, b):
#     return a + b

# print(type(lambda_func))
# print(type(plus))


# print(lambda_func(2, 3))
# print(plus(3, 2))


# def up_letter(word: str) -> str:
#     return word.title()

# def show_words(func, *sequence):
#     for i in sequence:
#         print(func(i))
#
# show_words(lambda w: w.upper(), 'ru', 'ua', 'tr', 'kz', 'uk')

# show_words(up_letter, ['nooruz', 'kgz', 'bishkek']
