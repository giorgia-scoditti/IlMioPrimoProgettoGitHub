"""
LEZIONE DEL 08/10/2026 - WEEK 03
"""
class Studente:
    def __init__(self, matricola, nome, cognome, data_nascita):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        # Ma come rappresento quelle che nelle basi di dati sono le relazioni?
        # Di seguito, un esempio.
        self.iscritto_a = None # Qui dentro ci finirà il riferimento ad un corso.

        @property
        def matricola(self):
            return self.matricola

        @matricola.setter
        def matricola(self, matricola):
            self.matricola = matricola

    def __str__(self):
        return f"{self.matricola}, {self.nome}, {self.cognome}, {self.data_nascita}"

    def iscriviti(self, corso):
        self.iscritto_a = corso

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
        self.lista_studenti = []
        self.__lista_studenti_iscritti = [] # Questo è il contenitore di studenti iscritti a questo corso.

    def __str__(self):
        return f"{self.codice}, {self.titolo}, {self.docente}"

    # Creo il metodo con cui io posso dall'esterno iscrivere un nuovo studente al corso in questione.
    def iscrivi_studente(self, studente):
        if len(self.__lista_studenti_iscritti) < 2:
            self.__lista_studenti_iscritti.append(studente)
        else:
            print("Errore, troppi studenti!")


def main():
    s1 = Studente("1234", "Mario", "Rossi", "20201014")
    print(s1)

    s2 = Studente("5678", "Gianni", "Blu", "20190925")
    print(s2)

    lista_studenti = [s1]
    lista_studenti.append(s2)

    c001 = Corso("001", "Programmazione Avanzata", "Lamberti")

    # Di seguito, creo un collegamento tra lo studente e il corso.
    s1.iscriviti(c001)
    # Di seguito invece, creo un collegamento tra il corso e lo studente.
    c001.iscrivi_studente(s1)
    c001.iscrivi_studente(s2)
    c001.iscrivi_studente(Studente("7777", "Luigia", "Arancioni", "20180606"))

main()



"""
LEZIONE DEL 12/10/2026 - WEEK 04
"""
# Studiamo il concetto di ereditarietà.
class Persona:
    def __init__(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome

    def __str__(self):
        return f"{self.__nome}, {self.__cognome}"

p1 = Persona("Michela", "Blu")

# Per dire che la classe Docente eredita dalla classe Persona, devo inserire il nome della classe Persona tra parentesi.
# Persona è la classe PADRE, mentre Docente è la classe FIGLIA.
class Docente(Persona):
    def __init__(self, nome, cognome, dipartimento):
        # NON DEVO RIPETERE GLI ATTRIBUTI DELLA CLASSE PADRE!
        # DI SEGUITO, TROVO L'ISTRUZIONE CHE COSTRUISCE LA PARTE PERSONA DEL DOCENTE.
        super().__init__(nome, cognome)
        # SOLO ORA POSSO INIZIALIZZARE GLI ATTRIBUTI SPECIFICI DEL DOCENTE.
        self.dipartimento = dipartimento

d1 = Docente("Alberto", "Azzurri", "DAUIN")

# Partendo dalle slide (n. 38), creo altre classi per seguire l'esempio.
class Employee:
    def __init__(self, name, wage):
        self.__name = name
        self.__wage = wage

    @property
    def wage(self):
        return self.__wage

    @wage.setter
    def wage(self, wage):
        self.__wage = wage

    def __str__(self):
        return f"{self.__name}, {self.__wage}"

    def increment_wage(self):
        self.__wage += 5000

e1 = Employee("Mr. Bean", 15000)
print(e1)

class Manager(Employee):
    def __init__(self, name, wage, managedUnit):
        super().__init__(name, wage)
        self.__managedUnit = managedUnit # Nella OOP si scrive così, non managed_unit.

    # Con la OOP, posso andare a ridefinire i metodi del PADRE che non mi piacciono, andando a specificare i comportamenti specializzati nel FIGLIO.
    def __str__(self):
        return f"{super().__str__()}, {self.__managedUnit}" # Prima chiamo la funzione per stampare la parte interna, poi aggiungo la parte specifica.

    # I metodi ridefiniti nei FIGLI con lo stesso nome, si dicono in OVERRIDING.
    def increment_wage(self):
        self.wage += 10000

m = Manager("B. Boss", 40000, "HR")
print(m)
print()

print("---Incremento della paga---")
e1.increment_wage()
print(e1)
m.increment_wage()
print(m)
print()

class Car:
    def __init__(self, license_plate, color, turned_on):
        self.license_plate = license_plate
        self.color = color
        self.turned_on = turned_on

    def __str__(self):
        return f"{self.license_plate}, {self.color}, {self.turned_on}"

c1 = Car("AB123CD", "Rossa", "False")

print("---Struttura dati---")
users = []
users.append(e1)
users.append(m)
# Di seguito, il fenomeno del DUCK TYPING.
# Si ha un contenitore in cui si possono inserire diversi tipi di elementi.
users.append("abcdefg")
users.append(35)
users.append(c1)

for user in users:
    print(str(user))