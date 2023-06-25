# print(2 + 3 * 6 - 3)
# print(2 ** 3)
# print(2 + 5 * 6 / 2.2)
# print(2 + 5 * 6 // 2.2)
# print("Tomek " * 4)
# print([1,2,3] * 3)
# print("Tomek" + "Tomek")
# print("Tomek" , "Tomek")
# print([1,2,3] + [4,5,6])
# print([1,2,3] + ["Tomek","Asia"])
#
# x = 10
# y = 6
#
# z = x + y
#
# z = z + x
# z += x
#
# print(x > y)
# print(x < y)
# print(x == y)
# print(x != y)
# print(x <= y)
# print(x >= y)
import random

# totolotek = {12,25,33,41,12,33}
# print(totolotek)

zbior = set()

def dodaj_liczby(liczba):
    zbior.add(liczba)
    print(zbior)


for i in range(5):
    dodaj_liczby(random.randint(1,10))


nowa_lista = list(zbior)
nowa_lista.sort()
print(nowa_lista)



pacjenci = ["Tomasz", "Adam", "Robert", 'Inga']

print(random.choice(pacjenci))
