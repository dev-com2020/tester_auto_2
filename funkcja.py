# def drukuje():
#     print("drukuje...")
#
#
# def dodawanie(a=0, b=0):
#     suma = a + b
#     return suma
#
#
# print("A tutaj coś innego z programu głównego...")
#
# for i in range(5):
#     drukuje()
#
# wyniki = []
# wyniki.append(dodawanie(5, 5))
# wyniki.append(dodawanie(22, 533))
# wyniki.append(dodawanie(52223, 53333))
# wyniki.append(dodawanie(52223))
# wyniki.append(dodawanie())
#
# print(wyniki)
#
# komunikat = "[Odmówił podania danych]"
# pacjenci = ["Tomasz", "Adam", "Robert", 'Inga']
#
# def pacjent(numer, imie=komunikat, nazwisko=komunikat):
#    return numer,imie,nazwisko
#
#
# kolejka = []
# for index,pc in enumerate(pacjenci):
#     kolejka.append(pacjent(index+1,pc))
#
# print(kolejka)





# pacjent(1)
# pacjent(2,'Tomasz')
# pacjent(3,nazwisko="Kowalski")
# pacjent(4,"","Kowalski")
# pacjent(imie="Robert")
#
#
# def parametry(*args):
#     for x in range(len(args)):
#         print(f"Parametry które dotarły do funkcji: {args[x]}")
#
#
# parametry()
# parametry(23)
# parametry(23,"tomek")
# parametry(23,"tomek",[4,5,6])

slownik = {1:"Tomek"}
slownik[2] = "Mariusz"
slownik[1] = "Adam"
slownik["Tomek"] = 2023
print(slownik['Tomek'])
# print(slownik['Adam'])
print(slownik.get('Adam'))
print(slownik.keys())
print(slownik.values())
print("Tomek" in slownik)