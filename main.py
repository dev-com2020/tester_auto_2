from pakiet import kalkulator,testy
from pakiet import kalkulator as k
from pakiet import human


# print("To jest główny plik...")
#
# kalkulator.mnozenie(10,2)
# kalkulator.dzielenie(50,2)
# k.dzielenie(55,22)
# k.mnozenie(100,3)
# print("Wynik odejmowania:",k.odejmowanie(50,10))
# testy.testy()


czlowiek1 = human.Human()
czlowiek1.imie = "Tomek"
czlowiek1.wiek = 40
czlowiek1.powitanie()
czlowiek1.jaka_plec()
czlowiek1.ile_mam_lat()

czlowiek2 = human.Human2("Ewa",20,"k")
czlowiek2.powitanie()
czlowiek2.jaka_plec()
czlowiek2.ile_mam_lat()

czlowiek3 = human.Human2('Adam',25,'m')
czlowiek3.powitanie()
czlowiek3.jaka_plec()
czlowiek3.ile_mam_lat()
