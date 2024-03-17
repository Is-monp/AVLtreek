import flet as ft
#funciones de estado.
async def button_clicked_byfilter(e):
    t.value = f"Se ha filtrado por: {color_dropdown.value}"
    await t.update_async()
    
async def button_clicked_bysort(e):
    y.value = f"Se ha sorteado por niveles:"
    await y.update_async()
    
async def button_clicked_bysearch(e):
        nodo_buscado.value = f"El nodo a buscar es: {field_search.value}"
        await nodo_buscado.update_async()
        
async def button_clicked_bydelete(e):
        nodo_eliminar.value = f"El nodo eliminar es: {field_delete.value}"
        await nodo_eliminar.update_async()


#Contenido de las tabs
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
    return ft.Column(controls=[leyenda, field_search,submit_buton, nodo_buscado])

def filter():
    global t, color_dropdown
    t = ft.Text()
    leyenda=ft.Text("Al clickear 'submit' se filtrará el arbol\nactual por el tipo de nodo seleccionado.")
    submitt_button = ft.FilledButton(text="Submit", on_click=button_clicked_byfilter,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    color_dropdown = ft.Dropdown(
        width=250,
        border_color=ft.colors.GREEN_400,
        height=55, 
        border_radius=20,
        hint_text="Selecciona el filtro:",
        options=[
            ft.dropdown.Option("Type "),
            ft.dropdown.Option("Size"),
        ]
    )
    return ft.Column(controls=[leyenda,color_dropdown, submitt_button, t])

def level_order():
    global y
    y = ft.Text()
    leyenda=ft.Text("Al clickear 'sort' se generara un recorrido\npor niveles del arbol actual.")
    submitt_button = ft.FilledButton(text="Sort", on_click=button_clicked_bysort,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.BLACK},bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_400}))
    return ft.Column(controls=[leyenda,submitt_button, y])

#Definicion de las tabs
def Tabs():
    t = ft.Tabs(
        selected_index=3,
        animation_duration=300,
        indicator_color=ft.colors.GREEN_400, label_color=ft.colors.GREEN_300,
        tabs=[
            ft.Tab(
                content=ft.Container(
                    content=ft.Column([ft.Text("this is tab1")])
                ),
                icon=ft.icons.ADD_CIRCLE_OUTLINED,
                text="Add node"
            ),
            ft.Tab(
                content=ft.Container(
                    content=delete_node(), alignment=ft.alignment.center, padding=ft.padding.only(top=60)
                ),
                icon=ft.icons.DELETE_FOREVER_OUTLINED,
                text="Delete node"
            ),
            ft.Tab(
                content=ft.Container(
                    content=search_node(), alignment=ft.alignment.center, padding=ft.padding.only(top=60)
                ),
                icon=ft.icons.SEARCH,
                text="Search node"
            ),
            ft.Tab(
                content=ft.Container(
                    content=filter(), alignment=ft.alignment.center, padding=ft.padding.only(top=60)
                ), icon=ft.icons.FILTER_ALT_OUTLINED,
                text="Filter nodes"
            ),
            
            ft.Tab(
                content=ft.Container(
                    content=level_order(), alignment=ft.alignment.center,padding=ft.padding.only(top=50)
                ),icon=ft.icons.MOVE_DOWN_ROUNDED,
                text="Level order traversal"
                
            ),
            ft.Tab(
                content=ft.Text("This is Tab 6"), icon=ft.icons.CONTENT_PASTE_SEARCH
            ),
        ],
        expand=1,)
    return t

