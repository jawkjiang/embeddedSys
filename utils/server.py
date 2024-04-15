import uhttpd
import ujson
import machine

class Server:

    def __init__(self):
        self.server = uhttpd.Server()
        self.server.listen(8080)
        self.server.route('/', self.handler)

        self.uart0 = machine.UART(1, tx=17, rx=16, baudrate=9600)
        self.uart1 = machine.UART(2, tx=26, rx=25, baudrate=9600)
        self.uart_list = [self.uart1, self.uart2]

    def handler(self, request):
        if request.method == 'POST':
            data = ujson.loads(request.data)
            uart = self.uart_list[data['uart']]
            uart.write(data['data'])
            return 'OK'
        
    def run(self):
        print('Server is running')
        self.server.run()

if __name__ == '__main__':
    server = Server()
    server.run()
