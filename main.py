import flet as ft
from tabs import Tabs
from visuals import Slider, images_slider


def main(page: ft.Page):
#Deficion de los componentes principales de la GUI.
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400        # window's width is 200 px
    page.window_height = 900       # window's height is 200 px
    page.window_resizable = False
    tabs = Tabs()
    this_slider=Slider(page)
    images = ft.Row(expand=1, wrap=False, scroll="always")
    route_list=[f"./data/cats/cat.{i}.jpg" for i in range(1, 20)]

    #Header con el nombre del proyecto y el slider para cambiar el tema.
    header=ft.Container(
        content=ft.Row([ft.Icon(name=ft.icons.ACCOUNT_TREE_ROUNDED, color=ft.colors.GREEN_500,size=50),ft.Text("ALVTrek", weight=ft.FontWeight.BOLD,size=20),this_slider]),
        alignment=ft.alignment.center,
        width=1400,
        height=50,         
    )
    #Galery (right side of the GUI).
    gallery = ft.Container(
        content=images,
        alignment=ft.alignment.center,
        margin=ft.margin.only(bottom=18),
        width=400,
        height=270
    )
    images_slider(route_list, images)
    
        
    SECONDARY_GUI = ft.Container(
        margin=ft.margin.only(bottom=9),
        expand=True,
        content=ft.Column([tabs,ft.Divider(height=1, color="green"),gallery])
    )
    
    MAIN_GUI = ft.Container(
        content=ft.Column([header, SECONDARY_GUI]),
        expand=True
    )
    page.add(MAIN_GUI)
    page.update()
    gallery.update()

if __name__ == '__main__':
    ft.app(target=main)