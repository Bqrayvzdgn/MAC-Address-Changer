import subprocess
import argparse
import re

Logo = """
██████╗░░██████╗░██████╗░██████╗░███████╗██╗░░░██╗
██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║
██████╦╝██║██╗██║██████╔╝██║░░██║█████╗░░╚██╗░██╔╝
██╔══██╗╚██████╔╝██╔══██╗██║░░██║██╔══╝░░░╚████╔╝░
██████╦╝░╚═██╔═╝░██║░░██║██████╔╝███████╗░░╚██╔╝░░
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░
"""

def get_user_input():
    parser = argparse.ArgumentParser(description="This application was developed by kenxzz.", usage="python macchanger.py -h", epilog="[ Default ] python3 macchanger.py -i [interface] -m [XX:XX:XX:XX:XX:XX]")
    parser.add_argument("-i", "--iface", dest="interface", help="Interface to change!")
    parser.add_argument("-m", "--mac", dest="mac_address", help="New mac address")
    parser.add_argument("-r", "--random", action="store_true", help="Generate a random MAC address")
    return parser.parse_args()

def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

if __name__ == "__main__":
    print(Logo)
    (user_input,arguments) = get_user_input()
    change_mac_address(user_input.interface,user_input.mac_address)
    finalized_mac = control_new_mac(str(user_input.interface))

    if finalized_mac == user_input.mac_address:
        print("MAC Address is created!")
    else:
        print("An error occurred while creating the MAC Address!")