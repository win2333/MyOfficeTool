from nicegui import app, ui
import logging

# 初始化日志
logging.basicConfig(level=logging.INFO)
# 初始化客户端数量为 0
client_count = 0


def submit():
    # 获取每个输入框的值并打印
    values = [field1.value, field2.value, field3.value, field4.value, field5.value, field6.value, field7.value, field8.value, field9.value]
    print("提交的值:", values)

# 创建第一行
with ui.row():
    # 创建第一个输入框并添加到第一列
    with ui.column():
        field1 = ui.input('字段 1')
    # 创建第二个输入框并添加到第二列
    with ui.column():
        field2 = ui.input('字段 2')
    # 创建第三个输入框并添加到第三列
    with ui.column():
        field3 = ui.input('字段 3')

# 创建第二行
with ui.row():
    # 创建第四个输入框并添加到第一列
    with ui.column():
        field4 = ui.input('字段 4')
    # 创建第五个输入框并添加到第二列
    with ui.column():
        field5 = ui.input('字段 5')
    # 创建第六个输入框并添加到第三列
    with ui.column():
        field6 = ui.input('字段 6')

# 创建第三行
with ui.row():
    # 创建第七个输入框并添加到第一列
    with ui.column():
        field7 = ui.input('字段 7')
    # 创建第八个输入框并添加到第二列
    with ui.column():
        field8 = ui.input('字段 8')
    # 创建第九个输入框并添加到第三列
    with ui.column():
        field9 = ui.input('字段 9')

# 创建提交按钮
ui.button('提交', on_click=submit)

with ui.row():
    # 创建侧边栏
    with ui.column():
        ui.label("侧边栏")
        ui.button("按钮 1")
        ui.button("按钮 2")
        
    # 创建主内容区
    with ui.column():
        ui.label("这是主内容区")


from nicegui import ui

with ui.expansion('Expand!', icon='work').classes('w-full'):
    with ui.tabs().classes('w-full') as tabs:
        one = ui.tab('One')
        two = ui.tab('Two')
        three = ui.tab('three')
        four = ui.tab('four')
        five = ui.tab('five')
    with ui.tab_panels(tabs, value=two).classes('w-full'):
        with ui.tab_panel(one):
            ui.label('First tab')
        with ui.tab_panel(two):
            ui.label('Second tab')
        with ui.tab_panel(three):
            ui.label('Three tab')
        with ui.tab_panel(four):
            ui.label('Fourth tab')
        with ui.tab_panel(five):
            ui.label('Fifth tab')





#关闭标签页和服务器的关系
def handle_connect(client):
    global client_count
    client_count += 1
    logging.info(f"New client connected. Total clients: {client_count}")

def handle_disconnect(client):
    global client_count
    client_count -= 1
    logging.info(f"Client disconnected. Remaining clients: {client_count}")

    # 检查客户端数量，如果为 0，则关闭服务器
    if client_count < 0:
        logging.warning("Client count is negative, correcting to 0.")
        client_count = 0

    if client_count == 0:
        logging.info("No clients remaining, shutting down.")
        app.shutdown()

# 注册事件处理函数
app.on_connect(handle_connect)
app.on_disconnect(handle_disconnect)

# 启动服务器
ui.run()
