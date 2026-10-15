"""
LEZIONE DEL 15/10/2026 - WEEK 04
"""
import operator

# Tutto il concetto dell'ereditarietà comincia dalla classe generica Object.
# La classe Object definisce dei metodi che altri possono andare a predefinire.
class LaMiaClasse:
    def __init__(self, attributo):
        self.attributo = attributo

    def __str__(self):
        return f"{self.attributo}"

    # Posso ridefinire il metodo __eq__ che è il metodo di confronto (in override).
    # Vado a scrivere al suo interno l'algoritmo di confronto.
    def __eq__(self, other):
        if self.attributo == other.attributo:
            return True
        else:
            return False

    def __repr__(self):
        return f"{type(self)} {self.attributo}"

# Come faccio a confrontare o1 e o2? Di seguito, vedrai che sono diversi.
o1 = LaMiaClasse("Pippo")
print(str(o1))
o2 = LaMiaClasse("Topolino")
print(str(o2))

if o1 == o2:
    print("Sono uguali")
else:
    print("Sono diversi")
print()

# Faccio la controprova. Risultano diversi anche qui.
# Perchè?
o3 = LaMiaClasse("Pippo")
print(str(o3))
o4 = LaMiaClasse("Pippo")
print(str(o4))

if o3 == o4:
    print("Sono uguali")
else:
    print("Sono diversi")
print()

# PYTHON USA LA VERSIONE __eq__ base, che guarda i riferimenti.
# Per confrontare le stringhe devo ridefinire __eq__. L'ho fatto sopra (sotto __str__).

# Di seguito, la funzione __repr__.
print(o1.__repr__())

# Una classe può avere tantissime righe di codice, ma questo codice devo scriverlo? NO!
# Posso usare @dataclass, che mi consente di scrivere una classe come contenitore, senza dover riscrivere a mano tutti i metodi (nella loro versione base).
# Da qui, ci siamo spostati al quinto power point.
# PER CREARE UNA CARTELLA in cui inserire i file, CREA UA PYTHON PACKAGE (companies).

# Di seguito, l'ordinamento secondo un certo valore.
print("---------------")
lista = [o1]
lista.append(o2)
lista.append(LaMiaClasse("Gastone"))
orderedList = lista.sort(key=operator.attrgetter("attributo"))
print(orderedList)