def drukuje():
    print("drukuje...")


def dodawanie(a=0, b=0):
    suma = a + b
    return suma


print("A tutaj coś innego z programu głównego...")

for i in range(5):
    drukuje()

wyniki = []
wyniki.append(dodawanie(5, 5))
wyniki.append(dodawanie(22, 533))
wyniki.append(dodawanie(52223, 53333))
wyniki.append(dodawanie(52223))
wyniki.append(dodawanie())

print(wyniki)

komunikat = "[Odmówił podania danych]"
pacjenci = ["Tomasz", "Adam", "Robert", 'Inga']

def pacjent(numer, imie=komunikat, nazwisko=komunikat):
   return numer,imie,nazwisko


kolejka = []
for index,pc in enumerate(pacjenci):
    kolejka.append(pacjent(index+1,pc))

print(kolejka)





# pacjent(1)
# pacjent(2,'Tomasz')
# pacjent(3,nazwisko="Kowalski")
# pacjent(4,"","Kowalski")
# pacjent(imie="Robert")


