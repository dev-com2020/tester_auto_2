class Human:

    def __init__(self):
        self.imie = '.'
        self.wiek = 0
        self.plec = 'm'

    def powitanie(self):
        print("Nazywam się", self.imie)

    def ile_mam_lat(self):
        print(f"mam {self.wiek} lat")

    def jaka_plec(self):
        if self.plec == 'm':
            print("Jestem mężczyzną")
        else:
            print("Jestem kobietą")


class Human2:

    def __init__(self, imie, wiek, plec):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print("Nazywam się", self.imie)

    def ile_mam_lat(self):
        print(f"mam {self.wiek} lat")

    def jaka_plec(self):
        if self.plec == 'm':
            print("Jestem mężczyzną")
        else:
            print("Jestem kobietą")
