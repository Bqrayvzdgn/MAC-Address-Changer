import subprocess
import argparse
import re

class Banners:
    ERROR = """
    ███████╗██████╗░██████╗░░█████╗░██████╗░██╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║
    █████╗░░██████╔╝██████╔╝██║░░██║██████╔╝██║
    ██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗╚═╝
    ███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║██╗
    ╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝
"""

    LOGO = """
    ██████╗░░██████╗░██████╗░██████╗░███████╗██╗░░░██╗
    ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║
    ██████╦╝██║██╗██║██████╔╝██║░░██║█████╗░░╚██╗░██╔╝
    ██╔══██╗╚██████╔╝██╔══██╗██║░░██║██╔══╝░░░╚████╔╝░
    ██████╦╝░╚═██╔═╝░██║░░██║██████╔╝███████╗░░╚██╔╝░░
    ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░
"""

def get_user_input():
    print(Banners.LOGO)
    parser = argparse.ArgumentParser(description="This application was developed by kenxzz.", usage="python3 macchanger.py -i [interface] -m [XX:XX:XX:XX:XX:XX]", epilog="[Important] You must have sudo privileges for Mac Changer to work properly.!")
    parser.add_argument("-i", "--iface", dest="interface", help="Enter your network interface")
    parser.add_argument("-m", "--mac", dest="mac_address", help="Enter your mac address")
    return parser.parse_args()

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
    user_input = get_user_input()
    change_mac_address(user_input.interface, user_input.mac_address)
