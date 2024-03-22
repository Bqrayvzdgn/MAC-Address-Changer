import subprocess
import optparse
import re
import time


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


def get_user_input():
    parse_object = optparse.OptionParser(
        description="This tool was developed by bqrdev.",
        usage="python mac-changer.py -i [INTERFACE] -h [MAC_ADDRES]"
    )
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse_object.parse_args()


def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def control_new_mac(interface):
    output = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


if __name__ == "__main__":
    print(Banners.LOGO)
    (user_input, args) = get_user_input()
    change_mac_address(user_input.interface, user_input.mac_address)
    finalized_mac = control_new_mac(str(user_input.interface))
    try:
        change_mac_address(user_input.interface, user_input.mac_address)
        print(f"Your MAC Address has been created : {str(user_input.mac_address)}")
    finally:
        print("Exiting.")
        print(Banners.QUIT)
else:
    print(Banners.ERROR)
