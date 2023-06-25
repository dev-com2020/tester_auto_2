class Animal:

    def __init__(self,gatunek,szybkosc):
        self.__gatunek = gatunek
        self.szybkosc = szybkosc

    def poluj(self):
        print(f"Jestem {self.__gatunek}, rozpoczynam polowanie")

    def lataj(self):
        print(f'Latam z prędkością {self.szybkosc}')


class Ssak(Animal):

    def __init__(self, gatunek, szybkosc,umaszczenie):
        super().__init__(gatunek, szybkosc)
        self.umaszczenie = umaszczenie

    def __lataj(self):
        print("Sorry, ja jestem nielotem...")

    def wydaj_odglos(self):
        print("pipipipipi")





orzel = Animal('Bielik',50)
# orzel.__gatunek = "SŁOŃ"
orzel.poluj()
orzel.lataj()


lisek = Ssak("Lis",20,'zielony')
lisek.poluj()
lisek.lataj()
lisek.wydaj_odglos()