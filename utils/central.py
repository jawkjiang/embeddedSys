import uhttpd
import ujson

class Central:
    def __init__(self):
        self.server = uhttpd.Server()
        self.server.listen(8080)
        self.server.route('/', self.handler)