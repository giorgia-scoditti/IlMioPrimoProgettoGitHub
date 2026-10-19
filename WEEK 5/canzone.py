"""
LEZIONE DEL 19/10/2026 - WEEK 05
"""
class Canzone:
    def __init__(self, titolo, artista, anno, durata):
        self._titolo = titolo
        self._artista = artista
        self._anno = anno
        self._durata = durata

    def __str__(self):
        return f"{self._titolo}, {self._artista}, {self._anno}, {self._durata}"

    def __repr__(self):
        return f"{self.__class__.__name__}(titolo='{self._titolo}', artista='{self._artista}', anno='{self._anno}', durata='{self._durata}')"

    # Per consentire a 2 oggetti di confontarsi con ==, devo definire __eq__.
    # Uso l'algoritmo di confronto con i parametri self e other.
    def __eq__(self, other):
        if self._titolo == other._titolo and self._artista == other._artista:
            return True
        else:
            return False

    # Analogamente, se voglio che oggetti di tipo Canzone siano ordinabili, come faccio?
    # Posso andare a ridifinire (in override) il metodo __lt()__.
    def __lt__(self, other):
        if self._anno == other._anno:
            return self._durata < other._durata
        else:
            return self._anno < other._anno
    # Questo confronto, se è vero restituisce True, altrimenti False.
    # Se voglio ordinarle al contrario, metto > invece di <.
    # Per ordinarle x anno e, a parità di anno, x durata, aggiungo quell'if.