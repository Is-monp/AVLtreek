import flet as ft

def Navigation_rail():
    rail = ft.NavigationRail(
    selected_index=0,
    label_type=ft.NavigationRailLabelType.ALL,
    min_width=100,
    min_extended_width=400,
    #leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
    group_alignment=-0.9,
    destinations=[
        ft.NavigationRailDestination(
            icon=ft.icons.ADD_CIRCLE_OUTLINE,
            selected_icon=ft.icons.ADD_CIRCLE, 
            label="Add node",
        ),
        ft.NavigationRailDestination(
            icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
            selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
            label="Delete node",
        ),
        ft.NavigationRailDestination(
            icon=ft.icons.FIND_IN_PAGE_OUTLINED,
            selected_icon_content=ft.Icon(ft.icons.FIND_IN_PAGE),
            label_content=ft.Text("Search node"),
        ),
        ft.NavigationRailDestination(
            icon=ft.icons.FILTER_ALT_OUTLINED,
            selected_icon_content=ft.Icon(ft.icons.FILTER_ALT),
            label_content=ft.Text("Filter nodes"),
        ),
    ],
    on_change=lambda e: print("Selected destination:", e.control.selected_index)
)
    return rail
