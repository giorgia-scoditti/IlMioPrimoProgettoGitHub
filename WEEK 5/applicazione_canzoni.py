"""
LEZIONE DEL 19/10/2026 (pt.2) - WEEK 05
"""
from operator import attrgetter
from canzone import Canzone

c1 = Canzone("Someone like you", "Adele", 2011, "3:11")
c2 = Canzone("Yellow Submarine", "The Beatles", 1966, "4:01")
c3 = Canzone("Scrivile Scemo", "Pinguini Tattici Nucelari", 2020, "2:30")
c4 = Canzone("Someone like you", "Altro artista", 2012, "8:12")

# Voglio confrontare due canzoni.
# Se faccio come di seguito, il == confronta i riferimenti di c1 e c2.
# Questo confronto mi darà sempre che non sono uguali.
if c1 == c2:
    print("Canzoni uguali")
else:
    print("Canzoni non uguali")

# Dopo avere definito __eq__ nella classe Canzone, il confronto avviene correttamente.
if c1 == c4:
    print("Canzoni con titolo e artista uguali")
else:
    print("Canzoni con titolo e artista non uguali")

print()
print("Lista di canzoni:")
lista_canzoni = [c1, c2, c3]
lista_canzoni.append(Canzone("Nuova canzone", "Artista", 2020, "8:05"))
for canzone in lista_canzoni:
    print(canzone)

# Uso il metodo __lt__ per ordinare le canzoni.
print()
print("Lista di canzoni ordinata per anno e durata:")
lista_ordinata = sorted(lista_canzoni)
for canzone in lista_ordinata:
    print(canzone)

# Oppure ordino così.
# Se voglio ordinarle in modo decrescente, aggiungo reverse = True.
print()
print("Lista di canzoni ordinata per titolo:")
lista_ordinata2 = sorted(lista_canzoni, key=attrgetter("_titolo"))
for canzone in lista_ordinata2:
    print(canzone)

# Oppure ordino ancora così.
print()
print("Lista di canzoni ordinata per artista:")
lista_ordinata3 = sorted(lista_canzoni, key=lambda canzone: canzone._artista)
for canzone in lista_ordinata3:
    print(canzone)