"""
LEZIONE DEL 19/10/2026 (pt.3) - WEEK 05
"""
# Creo un'applicazione con flet.
# Creo un'applicazione grafica, usando classi di altri.
import flet as ft
import asyncio

async def main(page : ft.Page):
    my_text = ft.Text("Il mio testo", size = 24, color = "blue") # Ho creato un oggetto.
    page.controls.append(my_text) # Ho chiamato il metodo append.
    for i in range(1, 100):
        my_text.value = f"{i}"
        await asyncio.sleep(1)
        my_text.update()
    page.update()  # Ho chiamato il metodo update.

ft.run(main)