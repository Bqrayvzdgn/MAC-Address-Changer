import random
import string
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
    parser.add_argument("-r", "--random", dest="random", help="Random mac address")

    return parser.parse_args()

def get_random_mac_address():
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")

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
    user_input = get_user_input()
    
    if user_input.mac_address:
        change_mac_address(user_input.interface, user_input.mac_address)
        finalized_mac = control_new_mac(str(user_input.interface))

        if finalized_mac == user_input.mac_address:
            print("MAC Address is successfully changed!")
        else:
            print("An error occurred while changing the MAC Address!")
    else:
        random_mac = get_random_mac_address()
        print("Randomly generated MAC Address:", random_mac)
