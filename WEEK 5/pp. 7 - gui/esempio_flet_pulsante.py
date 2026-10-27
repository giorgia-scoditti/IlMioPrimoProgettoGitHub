"""
LEZIONE DEL 19/10/2026 (pt.4) - WEEK 05
"""
import flet as ft

def main(page : ft.Page):
    my_text = ft.Text("Hello in red", size = 34, color = "red")

    # Funzione invocata da Python Flet quando noi premiamo quel pulsante.
    # Funzione annidata: ho una funzione dentro un'altra funzione.
    def button_handler():
        print("L'utente ha premuto il pulsante")
        my_text.color = "yellow"
        my_text.update()

    my_button = ft.Button("Cambia colore :-)", on_click = button_handler)
    page.controls.append(my_text)
    page.controls.append(my_button)
    page.update()

ft.run(main)