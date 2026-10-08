"""
LEZIONE DEL 08/10/2026 - WEEK 03
"""
# CONTROLLA SE E' GIUSTO!
class Studente:
    def __init__(self, matricola, nome, cognome, data_nascita):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita

    @property
    def matricola(self):
        return self.matricola

    @matricola.setter
    def matricola(self, matricola):
        self.matricola = matricola

    def __str__(self):
        return f"{self.matricola}, {self.nome}, {self.cognome}, {self.data_nascita}"

"""
IMMAGINA DI CREARE UN NUOVO FILE E INSERIRE I SEGUENTI DATI.

from dataclasses import dataclass 
@dataclass
class Studente:
    __matricola: str
    __nome: str
    __cognome: str
    __data_nascita: str

POSSO CREARE LA CLASSE COSI.
"""

class Corso:
    def __init__(self, codice, titolo, docente):
        self.codice = codice
        self.titolo = titolo
        self.docente = docente

    def __str__(self):
        return f"{self.codice}, {self.titolo}, {self.docente}"


def main():
    s1 = Studente("1234", "Mario", "Rossi", "20201014")
    print(s1)

    s2 = Studente("5678", "Gianni", "Blu", "20190925")
    print(s2)

    lista_studenti = [s1]
    lista_studenti.append[s2]

    c001 = Corso("001", "Programmazione Avanzata", "Lamberti")

main()