import flet as ft

def theme_changed(e, page,slider):
    page.theme_mode = (
        ft.ThemeMode.DARK
        if page.theme_mode == ft.ThemeMode.LIGHT
        else ft.ThemeMode.LIGHT
    )
    slider.label = (
        "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
    )
    page.update()

def Slider(page):
    slider = ft.Switch(active_color=ft.colors.BLACK,label="Light theme", on_change=lambda e: theme_changed(e, page,slider))
    return slider
