import random
import string
import subprocess
import optparse
import re

Logo = """
██████╗░░██████╗░██████╗░██████╗░███████╗██╗░░░██╗
██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║
██████╦╝██║██╗██║██████╔╝██║░░██║█████╗░░╚██╗░██╔╝
██╔══██╗╚██████╔╝██╔══██╗██║░░██║██╔══╝░░░╚████╔╝░
██████╦╝░╚═██╔═╝░██║░░██║██████╔╝███████╗░░╚██╔╝░░
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░
"""
Logo1 = """
███████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░███░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░███░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░███░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░███░░▄▀░░░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░░░░░▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░████░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀░░▄▀▄▀░░█
█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░░░░░█░░░░▄▀▄▀▄▀░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░░░▄▀░░░░███
█░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░███░░░░░░░░░░░░░░█████░░░░░░█████
███████████████████████████████████████████████████████████████████████████████████████████████████
"""

def get_user_input():
    parse_object = optparse.OptionParser(description="This application was developed by kenxzz.", usage="python macchanger.py -h", epilog="[ Default ] python3 macchanger.py -i [interface] -m [XX:XX:XX:XX:XX:XX]")
    parse_object.add_option("-i", "--iface", dest="interface", help="Interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="New mac address")
    parse_object.add_option("-s", "--show", help="Network interface show", action="store_true")
    parse_object.add_option("-R", "--random", dest="random", help="Random mac address", action="store_true")
    parse_object.add_option('-r', '--reset', help="Reset to Original MAC", action="store_true")

    return parse_object.parse_args()

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

def change_mac_address(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

if __name__ == "__main__":
    print(Logo1)
    user_input = get_user_input()
    change_mac_address(user_input.interface, user_input.mac_address, user_input.random)
    finalized_mac = control_new_mac(str(user_input.interface))

    if finalized_mac == user_input.mac_address:
        print("Success!")
    else:
        print("Error!")
