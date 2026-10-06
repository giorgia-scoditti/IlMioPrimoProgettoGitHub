"""
LEZIONE DEL 05/10/2026 (pt.2) - WEEK 03
"""
# SE DEVO UTILIZZARE UNA CLASSE DEFINITA IN UN ALTRO FILE O MODULO DEVO USARE LE PAROLE CHIAVE IMPORT E FROM.
from OOP import Quadro
# Ora posso utilizzare la classe Quadro, ad es. per creare oggetti.
q = Quadro("Monet", "...", "...", "...")

# Posso stampare l'oggetto chiedendo a quest'ultimo di restituire la sua descrizione come stringa con il metodo __str()__.
print(q.__str__())
# Se ho definito la funzione __str()__ per l'oggetto, quando lo vado a stampare Python capisce che deve utilizzare quella funzione anziché stampare l'indirizzo memoria.
# Così, non serve neanche esplicitare .__str()__, viene invocata automaticamente.
print(q)

# Ma cosa me ne faccio di queste classi?
# Una volta definito un nuovo tipo di dato (il Quadro), posso creare delle collezioni di oggetti di quel tipo, ad es. una lista.
lista_di_quadri = []
lista_di_quadri.append(q)
lista_di_quadri.append(Quadro("Cezanne", "...", "..."))
lista_di_quadri.append(Quadro("Pollock", "...", "..."))

print("Lista di quadri: ")
for quadro in lista_di_quadri:
    print(quadro.__str__())