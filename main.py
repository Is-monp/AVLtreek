import flet as ft
from tabs import Tabs
from visuals import Slider, images_slider

def tree_display(image_path:str):
    main_display=ft.Container(
        content=ft.Image(
            src=image_path,
            width=800,
            height=650,
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
        ),
        margin=5,
        padding=10,
        alignment=ft.alignment.center,
        width=800,
        height=650        
    ) 
    return main_display      
    

def main(page: ft.Page):
#Deficion de los componentes principales de la GUI.
    page.theme_mode = ft.ThemeMode.LIGHT
    tabs = Tabs()
    this_slider=Slider(page)
    this_main=tree_display("./data/cats/cat.1.jpg")
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
    
    #Gridview (left side of the GUI).
    gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    tables = ft.Container(
        alignment=ft.alignment.center,
        width=320,
        height=650,
        content=gv
    )
    for i in range(100):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                alignment=ft.alignment.center,
                border=ft.border.all(1, ft.colors.GREEN_400),
                border_radius=ft.border_radius.all(5),
            )
        )  
        
    SECONDARY_GUI = ft.Container(
        margin=ft.margin.only(bottom=9),
        expand=True,
        content=ft.Column([tabs,ft.Divider(height=1, color="green"),gallery])
    )
    components = ft.Container(
        margin=ft.margin.only(bottom=10),
        expand=True,
        content=ft.Row([tables, this_main, SECONDARY_GUI])
    )
    
    MAIN_GUI = ft.Container(
        content=ft.Column([header, components]),
        expand=True
    )
    page.add(MAIN_GUI)
    page.update()
    tables.update()
    gallery.update()

if __name__ == '__main__':
    ft.app(target=main)