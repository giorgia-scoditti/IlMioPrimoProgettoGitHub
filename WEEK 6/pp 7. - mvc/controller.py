"""
LEZIONE DEL 26/10/2026 - WEEK 06
"""
import flet as ft
from model import Model

class Controller():
    def __init__(self, model : Model, view : ft.View):
        self._model = model
        self._view = view

    def handler_minus(self, e):
        # print("-")
        # v = int(my_text.value)
        # v = v - 1
        # my_text.value = v
        # my_text.update()
        self._model.valore = self._model.valore - 1
        # DOVREI DIRE ALLA VIEW/PAGE DI AGGIORNARSI
        self._view.aggiorna_GUI(self._model.valore)

    def handler_plus(self, e):
        # print("+")
        # v = int(my_text.value)
        # v = v + 1
        # my_text.value = v
        # my_text.update()
        self._model.valore = self._model.valore + 1
        # DOVREI DIRE ALLA VIEW/PAGE DI AGGIORNARSI
        self._view.aggiorna_GUI(self._model.valore)