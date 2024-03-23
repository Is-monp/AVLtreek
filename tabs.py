import flet as ft
from avl import AVLTree
from visuals import tree_display
from prettytable import PrettyTable
import os
global myTree
myTree=AVLTree()
global root
root=None
def addNode(key):
    global root
    global myTree
    root= myTree.insert(root, key)
    myTree.printLevelOrder(root)
    
def createTable(listOfLists):
    x = PrettyTable()
    x.field_names = ["Name", "Level", "Balance", "Father", "Grandfather", "Uncle"]
    for i in listOfLists:
        x.add_row(i)
    return x

def exportTable(table):
    with open('table.txt', 'w') as file:
        file.write(str(table))

#funciones de estado.
async def button_clicked_byfilter(e):
    global t
    t.value = f"El filtro es: {color_dropdown.value} y el rango es: {range_slider.start_value} - {range_slider.end_value}"
    await t.update_async()
    print(int(float(range_slider.start_value)), int(float(range_slider.end_value)))
    filtered_tree=myTree.getInfos(root, color_dropdown.value, int(float(range_slider.start_value)), int(float(range_slider.end_value)))
    print(filtered_tree)
    table=createTable(filtered_tree)
    exportTable(table)

    
async def button_clicked_bysort(e):
    y.value =myTree.getLevelOrder(root)
    await y.update_async()
    
async def button_clicked_bysearch(e):
        nodo_buscado.value =myTree.getInfo(root, myTree.search(root, field_search.value))
        nodo_buscado.value={
            "name":nodo_buscado.value[0],
            "level":nodo_buscado.value[1],
            "balance":nodo_buscado.value[2],
            "father":nodo_buscado.value[3],
            "grandfather":nodo_buscado.value[4],
            "uncle":nodo_buscado.value[5],
        }
        await nodo_buscado.update_async()
        
async def button_clicked_bydelete(e):
        nodo_eliminar.value =myTree.delete(root, field_delete.value)
        new_route=myTree.outputTree(root)
        tree_display(new_route)
        await nodo_eliminar.update_async()
        
async def button_clicked_byadd(e):
        nodo_añadir.value = field_add.value
        addNode(field_add.value)
        new_route=myTree.outputTree(root)
        tree_display(new_route)
        await nodo_añadir.update_async()
        
def button_clickedbyview(e):
    # Open ./output.png
    os.system("open ./output.png")
    pass
def button_clicked_table(e):
    # Open ./table.txt
    os.system("open ./table.txt")
    pass

    #slider
def slider_change_start(e):
    print(
        f"Slider change start, values are {e.control.start_value}, {e.control.end_value}"
    )

def slider_is_changing(e):
    print(
        f"Slider is changing, values are {e.control.start_value}, {e.control.end_value}"
    )

def slider_change_end(e):
    print(
        f"Slider change end, values are {e.control.start_value}, {e.control.end_value}"
    )

#Contenido de las tabs
def añadir_nodo():
    global nodo_añadir, field_add
    nodo_añadir=ft.Text()
    leyenda=ft.Text("Use el nombre del nodo para agregarlo.")
    field_add= ft.TextField(width=250, height=55,hint_text="¿Que nodo desea agregar?", border_radius=20,border_color=ft.colors.GREEN_400, )
    submit_buton= ft.ElevatedButton(text="Submit", on_click=button_clicked_byadd,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    return ft.Column(controls=[leyenda, field_add,submit_buton, nodo_añadir])

def delete_node():
    global nodo_eliminar, field_delete
    nodo_eliminar=ft.Text()
    leyenda=ft.Text("Use el nombre del nodo para eliminarlo.")
    field_delete= ft.TextField(width=250, height=55,hint_text="¿Que nodo desea eliminar?", border_radius=20,border_color=ft.colors.GREEN_400,)
    submit_buton= ft.ElevatedButton(text="Submit", on_click=button_clicked_bydelete,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    return ft.Column(controls=[leyenda, field_delete,submit_buton,nodo_eliminar])

def search_node():
    global nodo_buscado, field_search
    nodo_buscado=ft.Text()
    leyenda=ft.Text("Use el nombre del nodo para buscarlo.")
    field_search= ft.TextField(width=250, height=55,hint_text="¿Que nodo desea buscar?", border_radius=20,border_color=ft.colors.GREEN_400,)
    submit_buton= ft.ElevatedButton(text="Submit", on_click=button_clicked_bysearch,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    Ver_tabla= ft.ElevatedButton(text="Ver contenido", on_click=button_clicked_table,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    return ft.Column(controls=[leyenda, field_search,submit_buton, Ver_tabla, nodo_buscado])

def filter():
    global t, color_dropdown, range_slider
    t = ft.Text()
    leyenda=ft.Text("Al clickear 'submit' se filtrará el arbol\nactual segun la información proporcionada.\nPodrá visualizar el resultado en la parte\nizquierda de la pantalla.")
    leyenda2=ft.Text("Seleccione un rango para filtrar por size")
    range_slider = ft.RangeSlider(
        min=0,
        max=10000000,
        start_value=0,
        divisions=10000,
        end_value=1000000,
        inactive_color=ft.colors.GREEN_300,
        active_color=ft.colors.GREEN_700,
        overlay_color=ft.colors.GREEN_100,
        label="{value}"
    )
    submitt_button = ft.FilledButton(text="Submit", on_click=button_clicked_byfilter,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    Ver_tabla= ft.ElevatedButton(text="Ver contenido", on_click=button_clicked_table,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    color_dropdown = ft.Dropdown(
        width=250,
        border_color=ft.colors.GREEN_400,
        height=55, 
        border_radius=20,
        hint_text="Selecciona el type de nodo.",
        options=[
            ft.dropdown.Option("bike"),   
            ft.dropdown.Option("cars"),
            ft.dropdown.Option("cats"),
            ft.dropdown.Option("dogs"),
            ft.dropdown.Option("flowers"),
            ft.dropdown.Option("horses"),
            ft.dropdown.Option("human"),
        ]
    
    )
    return ft.Column(controls=[leyenda,color_dropdown,leyenda2,range_slider,submitt_button,Ver_tabla, t])

def level_order():
    global y
    y = ft.Text()
    leyenda=ft.Text("Al clickear 'sort' se generara un recorrido\npor niveles del arbol actual.")
    submitt_button = ft.FilledButton(text="Sort", on_click=button_clicked_bysort,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    return ft.Column(controls=[leyenda,submitt_button, y])

def Visualize():
    leyenda=ft.Text("Al clickear 'View' se generara\n una vista del arbol actual.")
    submitt_button = ft.FilledButton(text="Sort", on_click=button_clickedbyview,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    return ft.Column(controls=[leyenda,submitt_button])

#info
def get_Nodoabuscar():
    return field_search.value

def get_Nodoaeliminar():
    return field_delete.value

def get_Nodoaagregar():
    return field_add.value

def get_filter():
    return color_dropdown.value

def get_startrange():
    return range_slider.start_value

def get_endrange():
    return range_slider.end_value

#Definicion de las tabs
def Tabs():
    t = ft.Tabs(
        selected_index=3,
        animation_duration=300,
        indicator_color=ft.colors.GREEN_400, label_color=ft.colors.GREEN_300,
        tabs=[
            ft.Tab(
                content=ft.Container(
                    content=añadir_nodo(), alignment=ft.alignment.center, padding=ft.padding.only(top=90)
                ),
                icon=ft.icons.ADD_CIRCLE_OUTLINED,
                text="Add node"
            ),
            ft.Tab(
                content=ft.Container(
                    content=delete_node(), alignment=ft.alignment.center, padding=ft.padding.only(top=90)
                ),
                icon=ft.icons.DELETE_FOREVER_OUTLINED,
                text="Delete node"
            ),
            ft.Tab(
                content=ft.Container(
                    content=search_node(), alignment=ft.alignment.center, padding=ft.padding.only(top=90)
                ),
                icon=ft.icons.SEARCH,
                text="Search node"
            ),
            ft.Tab(
                content=ft.Container(
                    content=filter(), alignment=ft.alignment.center, padding=ft.padding.only(top=30)
                ), icon=ft.icons.FILTER_ALT_OUTLINED,
                text="Filter nodes"
            ),
            ft.Tab(
                content=ft.Container(
                    content=level_order(), alignment=ft.alignment.center,padding=ft.padding.only(top=90)
                ),icon=ft.icons.MOVE_DOWN_ROUNDED,
                text="Level order traversal"
                
            ),
            ft.Tab(
                content=ft.Container(
                    content=Visualize(), alignment=ft.alignment.center,padding=ft.padding.only(top=90)),
                icon=ft.icons.CONTENT_PASTE_SEARCH, text="Visualize tree",
            ),
        ],
        expand=1,)
    return t