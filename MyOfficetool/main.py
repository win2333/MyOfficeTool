import logging
from nicegui import app, ui


with ui.tabs().classes('w-full') as tabs:
    one = ui.tab('One')
    two = ui.tab('Two')
    three = ui.tab('3')
    four = ui.tab('4')
with ui.tab_panels(tabs, value=one).classes('w-full'):
    with ui.tab_panel(one):
        ui.label('First tab')
        checkbox = ui.checkbox('check me')
        ui.label('Check!').bind_visibility_from(checkbox, 'value')
    with ui.tab_panel(two):
        ui.label('Second tab')
    with ui.tab_panel(three):
        ui.label('three tab')


# 启动服务器
ui.run()
