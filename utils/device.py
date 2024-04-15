import machine
import time
import urequests
import ujson

class Device:

    def __init__(self, id):
        self.id = id
        self.central_url = 'http://192.168.1.100:8080'

        self.uart0 = machine.UART(1, tx=17, rx=16, baudrate=9600)
        self.uart1 = machine.UART(2, tx=26, rx=25, baudrate=9600)

    def run(self):
        print('Device is running')
        while True:
            if self.uart0.any():
                if self.uart0.read() == b'1':
                    self.interrupt_handler0(0)
            if self.uart1.any():
                if self.uart1.read() == b'1':
                    self.interrupt_handler1(0)
        time.sleep(0.1)

    def interrupt_handler0(self, pin):
        data = {
            'id': self.id,
            'data': '1'
        }
        request = urequests.post(self.central_url, data=ujson.dumps(data))
    def interrupt_handler1(self, pin):
        data = {
            'id': self.id,
            'data': '1'
        }
        request = urequests.post(self.central_url, data=ujson.dumps(data))


if __name__ == '__main__':
    device = Device(id=1)
    device.run()
