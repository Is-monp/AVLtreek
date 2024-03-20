import flet as ft
from tabs import Tabs
from visuals import Slider

def main(page: ft.Page):
#Deficion de los componentes principales de la GUI.
    page.theme_mode = ft.ThemeMode.LIGHT
    tabs = Tabs()
    this_slider=Slider(page)
    main_display=ft.Container(
        content=ft.Text("Area para mostrar cosas", size=20, color="Black"),
        margin=5,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.WHITE,
        width=800,
        height=650        
    )  
    

    header=ft.Container(
        content=ft.Row([ft.Icon(name=ft.icons.ACCOUNT_TREE_ROUNDED, color=ft.colors.GREEN_500,size=50),ft.Text("ALVTrek", weight=ft.FontWeight.BOLD,size=20),this_slider]),
        alignment=ft.alignment.center,
        width=1400,
        height=50,         
    )

    galery = ft.Container(
        content=ft.Text("Ver foto del nodo", size=10, color="Black"),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREEN_100,
        margin=ft.margin.only(bottom=18),
        width=400,
        height=270
    )
    
    tables = ft.Container(
        content=ft.Text("Table", size=10, color="Black"),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.PINK_100,
        width=320,
        height=650
    )
    SECONDARY_GUI = ft.Container(
        margin=ft.margin.only(bottom=9),
        expand=True,
        content=ft.Column([tabs,galery])
    )
    components = ft.Container(
        margin=ft.margin.only(bottom=10),
        expand=True,
        content=ft.Row([tables, main_display, SECONDARY_GUI])
    )
    
    MAIN_GUI = ft.Container(
        content=ft.Column([header, components]),
        expand=True
    )
    page.add(MAIN_GUI)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)