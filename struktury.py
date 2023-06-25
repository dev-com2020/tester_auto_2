dozwoloneWaluty = ('PLN','EUR','USD')
# waluta = input("Podaj walutę: ")
#
# if waluta in dozwoloneWaluty:
#     print("poprawna waluta")
# else:
#     print(f"Nieznany kod waluty, podano: {waluta}")
#     print("Nieznany kod waluty, podano: {}".format(waluta))
#     print("Nieznany kod waluty, podano: %s" % waluta)

lista = []
lista2 = ["Ania","Maciek",'Ula']



lista.append("Tomek")
lista.append("Robert")
lista.append("Mateusz")
lista.insert(1,'Zuzia')
lista.append(dozwoloneWaluty)
lista.pop(0)
lista.remove('Zuzia')
lista.append(lista2)
# lista.clear()
lista[0] = "Tomek"
# lista.sort()
lista.reverse()
# lista[1] = lista[2]
print(lista[0])
zmienna = lista[1:4]
ostatni = lista[-1][0]

print(lista)
# print(zmienna)
# print(ostatni)