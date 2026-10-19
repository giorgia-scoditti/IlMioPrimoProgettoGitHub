"""
LEZIONE DEL 19/10/2026 (pt.3) - WEEK 05
"""
from dataclasses import dataclass

# Il dataclass va a creare in automatico delle funzioni di stampa.
# Facendo come di seguito, crea anche un metodo di confronto __eq__ ed un metodo di ordinamento __lt__.
# Questi metodi usano TUTTI gli attributi.
@dataclass(eq=True, order=True)
class Canzone:
    _titolo : str
    _artista : str
    _anno : int (compare=False) # Così, escludo questo attributo.
    _durata : str

c = Canzone("T", "A", 1999, "5:23")
print(c)