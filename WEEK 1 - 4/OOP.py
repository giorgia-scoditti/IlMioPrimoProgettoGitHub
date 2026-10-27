"""
LEZIONE DEL 01/10/2026 - WEEK 02
"""
# Definizione di una classe (classe STUDENTE).
class Studente:
    # Attributi.
    matricola = 0
    nome = ""
    cognome = ""

    # COSTRUTTORE: funzione standard per inizializzare l'oggetto. Prepara la memoria pe lo studente.
    def __init__(self, matricola, nome, cognome): # SELF indica che è una funzione della classe.
        self.matricola = matricola # SELF significa "questo oggetto".
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



"""
LEZIONE DEL 05/10/2026 (pt.1) - WEEK 03
"""
# Definisco un nuovo tipo di dato, la classe Car.
class Car: # Per convenzione, le classi  hanno iniziale maiuscola.
    def __init__(self):
        # Attributi o variabili d'istanza.
        self.license_plate = ""
        self.color = "White"
        self.turned_on = False

c1 = Car() # Creo un oggetto di classe/tipo Car. La classe è un nuovo tipo di dato.
"""
print(c1) # NON STAMPO L'OGGETTO, MA IL RIFERIMENTO ALL'OGGETTO.
"""

c1.license_plate = "GE888EG" # Ma così, tutte le macchine avranno la stessa targa.
print(f"License plate: {c1.license_plate}")
print(f"Color: {c1.color}")
print(f"Turned on: {c1.turned_on}")
print()

# Allora, uso il costruttore. SI FA COSI!
class Car:
    wheels = 4 # Variabile di classe, identica per tutte le istanze di quella classe. Finisce all'interno dello stampino!
    def __init__(self, license_plate, color): # Costruttore della classe.
        self.license_plate = license_plate
        self.color = color
        self.turned_on = False

    # METODI DI CUI PARLO SOTTO, NELLA RIGA 110. Sono le funzioni messe a disposizione di una classe.
    def paint(self, color):
        self.color = color

    def turn_on(self):
        self. turned_on = True

# CREO 2 OGGETTI DIVERSI, USANDO LO STESSO STAMPINO. OGNUNO DI LORO HA I PROPRI DATI.
c1 = Car("AA123BB", "Red") # Invoco il costruttore passando solo 2 argomenti perchè il costruttore riceve solo 2 parametri.
print(f"License plate: {c1.license_plate}")
print(f"Color: {c1.color}")
print(f"Turned on: {c1.turned_on}")
print()

c2 = Car("ZZ666ZZ", "Black")
print(f"License plate: {c2.license_plate}")
print(f"Color: {c2.color}")
print(f"Turned on: {c2.turned_on}")
print()

# Quindi, come si accede alle variabili d'istanza?
c1. color = "Green"
# E alle variabili di classe?
Car.wheels = 7 # Ho cambiato in memoria lo stampino.

# Ma ora, come posso cambiare il colore di un oggetto Car?
c1. color = "Pink"
# E lo stato di un oggetto Car?
c1.turned_on = True
# Dunque, per modificare la configurazione delle mie istanze, basta prendere l'oggetto e cambiarlo.
# Ma, potrei anche inserire all'interno della classe, dei metodi per fare queste operazioni (LI HO AGGIUNTI SOPRA).
# USA I METODI, ANZICHE ACCEDERE DIRETTAMENTE AGLI ATTRIBUTI!
c1.paint("Violet")
c2.turn_on()

# Di seguito ho una variabile di classe, di istanza o altro?
# Il programmatore può, tipicamente per sbaglio, andare a definire delle altre variabili scrivendo nome_oggetto.nome_variabile.
# Questa variabile sarà propria solo di quella istanza e non di tutti gli oggetti creati a partire da quella classe.
c1.number_of_doors = 2

# Ora creo una nuova classe. Parliamo di visibilità.
class Quadro:
    def __init__(self, artista, titolo, materiali, anno):
        self.__artista = artista
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno

    def imposta_anno(self, nuovo_anno):
        if nuovo_anno > 1853 and nuovo_anno < 1890:
            self.__anno = nuovo_anno
        else:
            print(f"L'anno inserito non è valido")

    def leggi_anno(self):
        return self.__anno

q1 = Quadro("Van Gogh", "Autoritratto", "Olio su tela", 1870)

""""
print(f"{q1.__artista} - {q1.__titolo} - {q1.__materiali} - {q1.__anno}")
# ERRORE 1: non mi stampa nulla perchè queste proprietà sono private.
# Per poterle leggere mi serve una funzione che me le restituisca.

q1.__anno = 1945 
# ERRORE 2: tratto qusti attributi come se fossero delle normali variabili.
# Se voglio cambiare l'anno, non posso farlo così perchè l'attributo è privato/nascosto (__).
"""
# Ad esempio, per stampare l'anno devo fare così.
print(f"Anno: {q1.leggi_anno()}")
# Per accedere all'attributo devo usare i metodi/le funzioni!
q1.imposta_anno(1800)

# COSI, IL CODICE DIVENTA INUTILMENTE COMPLICATO!!
# POSSO USARE I METODI GETTER E SETTER PER L'ACCESSO AGLI ATTRIBUTI IN LETTURA E SCRITTURA.
# Di seguito, ricopio il codice e utilizzo quei metodi.
class Quadro:
    def __init__(self, artista, titolo, materiali, anno):
        # Attributi privati/nascosti. Uso _ per scoraggiare o __ per bloccare l'accesso.
        self.__artista = artista
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno

    # Metodo per leggere il valore dell'attributo nascosto anno. METODO GETTER.
    @property
    def anno(self):
        return self.__anno

    # Metodo per impostare il valore dell'attributo nascosto anno. METODO SETTER.
    @anno.setter
    def anno(self, anno):
        self.__anno = anno # Eventualmente posso aggiungere il codice per il controllo degli errori.

    # Metodo/funzione che permette al quadro di descriversi come stringa.
    # Uso __str__ come alternativa a nomi più bizzarri.
    def __str__(self):
        return f"{self.__artista} - {self.__titolo} - {self.__materiali} - {self.anno}"

q1 = Quadro("Van Gogh", "Autoritratto", "Olio su tela", 1870)
print(f"Anno: {str(q1.anno)}")
print(q1)

# Non ha senso scrivere mille righe di codice!
# Ho DELEGATO al quadro il compito di stamparsi.
print(q1.__str__())

"""
IN CONCLUSIONE:
1. CON LE CLASSI POSSO DEFINIRE I MIEI TIPI DI DATO (ES. QUADRO).
2. POSSO DOTARLI DEI DATI/DEGLI ATTRIBUTI CHE LI CARATTERIZZNO (TENDENZIALMENTE NASCOSTI).
3. POSSO DOTARLI DELLE FUNZIONI/DEI METODI PER OPERARE SU QUEI DATI, OVVERO DEI METODI GETTER/SETTER (PER ACCEDERE AGLI ATTRIBUTI) O ALTRI (ES. __str__()))
"""