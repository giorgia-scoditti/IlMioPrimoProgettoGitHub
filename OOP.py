# Definizione di una classe (classe STUDENTE).
class Studente:
    # Attributi.
    matricola = 0
    nome = ""
    cognome = ""

    # COSTRUTTORE: funzione standard per inizializzare l'oggetto.
    def __init__(self, matricola, nome, cognome):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome

    # Altre funzioni.
    def sostiene_esame(self):
        print(f"Sostiene esame")

    def si_unisce_a_gruppo(self):
        print(f"Si unisce a un gruppo")

"""  
    def immatricola(self, m):
        self.matricola = m # Il self davanti serve per far sì che PyCharm capisca che deve riferirsi a ciò che ho scritto sopra.
"""

# Creazione di un oggetto / istanza (della classe STUDENTE).
# Accedo alla pancia di un oggetto per leggere i suoi attributi.
s = Studente(123456, "Mario", "Rossi") # Sto creando e inizalizzando uno studente. La s indica una variabile. Python chiama la funione __init__().

# Con la notazione puntata, ovvero il punto, posso accedere a ciò che sta nella pancia dell'oggetto s.
print(f"{s.matricola} - {s.nome} - {s.cognome}")
print()

# Posso invocare su QUELLO stuedente (Mario Rossi) la funzione che serve per fargli sostenere l'esame.
# Dati e operazioni su essi sono incapsulati nell'oggetto.
s.sostiene_esame()
print()

# Voglio creare una collezione (= contenitore) di studenti.
lista_studenti = []
lista_studenti.append(s)
lista_studenti.append(Studente(67890, "Gianni", "Verdi"))

for studente in lista_studenti:
    print(studente.matricola, studente.nome, studente.cognome)