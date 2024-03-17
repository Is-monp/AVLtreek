import flet as ft
from tabs import Tabs

def main(page: ft.Page):
    page.theme_mode = "dark"
    t = Tabs()
    main_display=ft.Container(
        content=ft.Text("Area para mostrar cosas", size=20, color="Black"),
        margin=5,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.WHITE,
        width=900,
        height=600        
    )    
    header=ft.Container(
        content=ft.Text("Header", size=20, color="black"),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREEN_400,
        width=1400,
        height=50
    )
    galery = ft.Container(
        content=ft.Text("Ver foto del nodo", size=10, color="Black"),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREEN_100,
        width=320,
        height=250
    )
    
    SECONDARY_GUI = ft.Container(
        margin=ft.margin.only(bottom=11),
        expand=True,
        content=ft.Column([t,galery])
    )
    components = ft.Container(
        margin=ft.margin.only(bottom=40),
        expand=True,
        content=ft.Row([main_display, SECONDARY_GUI])
    )
    
    MAIN_GUI = ft.Container(
        content=ft.Column([header, components]),
        expand=True
    )
    page.add(MAIN_GUI)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)