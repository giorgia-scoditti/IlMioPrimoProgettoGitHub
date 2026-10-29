"""
LEZIONE DEL 26/10/2026 - WEEK 06
"""
import flet as ft

class View():

    def __init__(self, page : ft.Page):
        self._page = page
        self._controller = None


    def imposta_controller(self, controller):
        self._controller = controller
        self.inizializza_GUI()

    def inizializza_GUI(self):
        self._page.window.width = 420
        self._page.window.height = 300
        self._page.vertical_alignment = ft.MainAxisAlignment.CENTER

        my_button_minus = ft.IconButton(icon=ft.Icons.REMOVE,
                                        icon_size=50,
                                        on_click=self._controller.handler_minus)

        my_button_plus = ft.IconButton(icon=ft.Icons.ADD,
                                       icon_size=50,
                                       on_click=self._controller.handler_plus)

        self._my_text = ft.TextField(value=0,
                               disabled=True,
                               width=100,
                               text_size=50,
                               text_align=ft.TextAlign.CENTER
                               )

        my_row = ft.Row([my_button_minus, self._my_text, my_button_plus],
                        alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(my_row)

    def aggiorna_GUI(self, v):
        self._my_text.value = v
        self._page.update()