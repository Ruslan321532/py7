ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
square_evens = list(map(lambda x: x**2, evens))
# print(square_evens, evens)


def print_index(index, mylist=ten):
    try:
        print(mylist[index])
    except IndexError:
        print(
            f"уkaзанный индекс ({index}) не допустим. Введите коректный индекс (от 0 до {len(mylist)-1}).")


while True:
    index = input("Введите индекс для вывода (z для выхода):")
    if index == "z":
        break
    else:
        try:
            index = int(index)
            print_index(index)
        except ValueError:
            print("Некорректный ввод")
