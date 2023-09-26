import logging



# 初始化日志
logging.basicConfig(level=logging.INFO)

# 初始化客户端数量为 0
client_count = 0
# 关闭标签页和服务器的关系
def handle_connect(_):
    global client_count
    client_count += 1
    logging.info(f"New client connected. Total clients: {client_count}")
def handle_disconnect(_):
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


import logging

class ClientManager:
    def __init__(self, app):
        self.client_count = 0
        self.app = app
        self.app.on_connect(self.handle_connect)
        self.app.on_disconnect(self.handle_disconnect)
        logging.basicConfig(level=logging.INFO)

    def handle_connect(self, _):
        self.client_count += 1
        logging.info(f"New client connected. Total clients: {self.client_count}")

    def handle_disconnect(self, _):
        self.client_count -= 1
        logging.info(f"Client disconnected. Remaining clients: {self.client_count}")

        # 检查客户端数量，如果为 0，则关闭服务器
        if self.client_count < 0:
            logging.warning("Client count is negative, correcting to 0.")
            self.client_count = 0

        if self.client_count == 0:
            logging.info("No clients remaining, shutting down.")
            self.app.shutdown()

# 假设 app 是你的应用实例
# app = YourAppInstance()
# client_manager = ClientManager(app)
