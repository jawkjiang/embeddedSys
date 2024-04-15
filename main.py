import dotenv

dotenv.load_dotenv()

if dotenv.get('isCentral') == 'True':
    from utils import Central
    central = Central()
    central.run()

else:
    from utils import Device
    device = Device()
    device.run()