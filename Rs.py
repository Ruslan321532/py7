# years = []
# for i in range(2000, 2020):
#     years.append(i)
#     years
#     print(years)


# a = [i for i in range(1, 15)]
# print(a)

# numbers = [1, 2, 3, 4, 5]  # = range(1,6)
# squares = []
# for number in numbers:
#     squares.append(number*number)
#     # squares = [1,4,9,16,25]
# print(number)
# Primes = [2, 3, 5, 7, 11, 13]
# Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(filter(lambda x: (x % 2 == 0), my_list))
# print(new_list)

tens = [lambda x=x: x*2 for x in range(1, 6)]
for table in tens:
    print(table())


