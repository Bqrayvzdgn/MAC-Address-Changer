import subprocess
import optparse
import re

def get_user_input():
    parse_object = optparse.OptionParser(description="macchanger [Option]", usage="python3 macchanger --help", epilog="[ Manual Mode ] python3 macchanger.py -i [interface] -m [XX:XX:XX:XX:XX:XX]")
    parse_object.add_option("-i", "--iface", dest="interface", help="Interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="New mac address")
    parse_object.add_option("-s", "--show", help="Network interface show", action="store_true")
    parse_object.add_option("-R", "--random", help="Random mac address", action="store_true")
    parse_object.add_option('-r', '--reset', help="Reset to Original MAC", action="store_true")
    return parse_object.parse_args()

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

def change_mac_address(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

if __name__ == "__main__":
    print("Macchanger started!")
    (user_input, arguments) = get_user_input()
    change_mac_address(user_input.interface, user_input.mac_address)
    finalized_mac = control_new_mac(str(user_input.interface))

    if finalized_mac == user_input.mac_address:
        print("Success!")
    else:
        print("Error!")