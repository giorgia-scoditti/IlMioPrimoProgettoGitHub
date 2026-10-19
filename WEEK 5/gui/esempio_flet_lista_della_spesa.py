"""
LEZIONE DEL 19/10/2026 (pt.5) - WEEK 05
"""
import flet as ft

def main(page : ft.Page):
    my_text_field = ft.TextField("Aggiungi un elemento:")
    my_list_view = ft.ListView

    def aggiungi_handler():
        my_list_view.append(ft.Checkbox(f"{my_text_field.value}"))
        page.update()

    my_button_add = ft.CupertinoButton(content = "Aggiungi", on_click = aggiungi_handler)
    row1 = ft.Row([my_text_field, my_button_add], alignment = ft.MainAxisAlignment.CENTER)
    # page.controls.append(my_text_field)
    # page.controls.append(my_button_add)
    page.controls.append(row1)
    page.controls.append(my_list_view)
    page.update()

ft.run(main)
# SISTEMA PER BENE!