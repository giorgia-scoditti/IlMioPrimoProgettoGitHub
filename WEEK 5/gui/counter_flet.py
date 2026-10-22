"""
LEZIONE DEL 22/10/2026 - WEEK 05
"""
import flet as ft

def main(page : ft.Page):
    page.window.width = 420
    page.window.height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def handler_minus(e):
        print("-")
        v = int(my_text.value)
        v = v - 1
        my_text.value = v
        my_text.update()

    def handler_plus(e):
        print("+")
        v = int(my_text.value)
        v = v + 1
        my_text.value = v
        my_text.update()

    my_button_minus = ft.IconButton(icon = ft.Icons.REMOVE, icon_size = 50, on_click = handler_minus)
    my_button_plus = ft.IconButton(icon = ft.Icons.ADD, icon_size = 50, on_click = handler_plus)
    my_text = ft.TextField(value = 0, disabled = True, width = 100, text_size = 50, text_align = ft.TextAlign.CENTER)

    my_row = ft.Row([my_button_minus, my_text, my_button_plus], alignment = ft.MainAxisAlignment.CENTER)

    page.controls.append(my_row)

    """
    page.controls.append(my_button_minus)
    page.controls.append(my_text)
    page.controls.append(my_button_plus)
    """

    page.update()

ft.run(main)