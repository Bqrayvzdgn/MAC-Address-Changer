import subprocess
import re

class Banners:
    ERROR = """
    ▒█▀▀▀ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ █ 
    ▒█▀▀▀ ▒█▄▄▀ ▒█▄▄▀ ▒█░░▒█ ▒█▄▄▀ ▀ 
    ▒█▄▄▄ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ ▒█░▒█ ▄
    """

    QUIT = """
    ▒█▀▀▀█ ▒█▀▀▀ ▒█▀▀▀ ▒█░░▒█ ▒█▀▀▀█ ▒█░▒█ 
    ░▀▀▀▄▄ ▒█▀▀▀ ▒█▀▀▀ ▒█▄▄▄█ ▒█░░▒█ ▒█░▒█ 
    ▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄▄ ░░▒█░░ ▒█▄▄▄█ ░▀▄▄▀
    """

    LOGO = """
    ▒█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▄ ▒█▀▀▀ ▒█░░▒█ 
    ▒█▀▀▄ ▒█░▒█ ▒█▄▄▀ ▒█░▒█ ▒█▀▀▀ ░▒█▒█░ 
    ▒█▄▄█ ░▀▀█▄ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄ ░░▀▄▀░
    """

def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])
    finalized_mac = control_new_mac(user_interface)
    if finalized_mac == user_mac_address:
        print("MAC Address is created!")
    else:
        print(Banners.ERROR)

def control_new_mac(interface):
    output = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    if new_mac:
        return new_mac.group(0)
    else:
        return None
    
if __name__ == "__main__":
    iface = input(str("Enter the network interface: "))
    macaddr = input(str("Enter the Mac address: "))
    try:        
        change_mac_address(iface, macaddr)
    except KeyboardInterrupt:
        print("Exiting.")
    finally:
        print(Banners.QUIT)
else:
    print(Banners.ERROR)
