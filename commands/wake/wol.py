from wakeonlan import send_magic_packet
import json

f = open('files/macs.json')
macs = json.load(f)

def send_magic_packet(name):
    try:
        mac_address = macs[name]
        send_magic_packet(mac_address, interface='192.168.1.1')
        return True
    except:
        return False
