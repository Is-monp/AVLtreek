import flet as ft

color_dropdown = ft.Dropdown(
    width=200,
    label="Filtro",
    hint_text="Selecciona el filtro:",
    options=[
        ft.dropdown.Option("Por type "),
        ft.dropdown.Option("Por size"),
    ],
)    

header=ft.Container(
    content=ft.Text("Header", size=20, color="black"),
    alignment=ft.alignment.center,
    bgcolor=ft.colors.GREEN_400,
    width=20,
    height=20
)
    
def Tabs():
    t = ft.Tabs(
        selected_index=3,
        animation_duration=300,
        indicator_color=ft.colors.GREEN_400, label_color=ft.colors.GREEN_200,
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
                    content=ft.Text("This is Tab 2"), alignment=ft.alignment.center,
                ),
                icon=ft.icons.DELETE_FOREVER_OUTLINED,
                text="Delete node"
            ),
            ft.Tab(
                content=ft.Container(
                    content=ft.Text("This is Tab 3"), alignment=ft.alignment.center
                ),
                icon=ft.icons.SEARCH,
                text="Search node"
            ),
            ft.Tab(
                content=ft.Container(
                    content=ft.Column([color_dropdown]),alignment=ft.alignment.center
                ), icon=ft.icons.FILTER_ALT_OUTLINED,
                text="Filter nodes"
            ),
            
            ft.Tab(
                content=ft.Container(
                    content=ft.Text("This is Tab 5"), alignment=ft.alignment.center
                ),icon=ft.icons.MOVE_DOWN_ROUNDED,
                text="Level order traversal"
                
            ),
            ft.Tab(
                content=ft.Text("This is Tab 6"), icon=ft.icons.CONTENT_PASTE_SEARCH
            ),
        ],
        expand=1,)
    return t

    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()