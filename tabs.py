import flet as ft
def Tabs():
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                content=ft.Text("This is Tab 4"),
            ),
            
            ft.Tab(
                content=ft.Text("This is Tab 5"),
            ),
        ],
        expand=1,)
    return t