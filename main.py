import flet as ft
from nav_rail import Navigation_rail
from tabs import Tabs

def main(page: ft.Page):
    page.theme_mode = "dark"
    n_rail = Navigation_rail()
    t = Tabs()
    main_display=ft.Container(
        content=ft.Text("Area para mostrar cosas", size=50, weight=ft.FontWeight.BOLD, color="Black"),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.WHITE,
        width=900,
        height=600        
    )
    MAIN_GUI = ft.Container(
        margin=ft.margin.only(bottom=40),
        expand=True,
        content=ft.Row([n_rail,main_display, t])
    )
    page.add(MAIN_GUI)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)