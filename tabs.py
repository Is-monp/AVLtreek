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
                icon=ft.icons.ADD,
            ),
            ft.Tab(
                content=ft.Text("This is Tab 2"),icon=ft.icons.MINIMIZE
            ),
            ft.Tab(
                content=ft.Text("This is Tab 3"),
                icon=ft.icons.SEARCH
            ),
            ft.Tab(
                content=ft.Text("This is Tab 4"), icon=ft.icons.SWIPE_OUTLINED
            ),
            
            ft.Tab(
                content=ft.Text("This is Tab 5"),icon=ft.icons.MOVE_DOWN_ROUNDED
            ),
            ft.Tab(
                content=ft.Text("This is Tab 6"), icon=ft.icons.CONTENT_PASTE_SEARCH
            ),
        ],
        expand=1,)
    return t