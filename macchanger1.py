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
    parser = argparse.ArgumentParser(Logo, description="This application was developed by kenxzz.", usage="python3 macchanger.py -i [interface] -m [XX:XX:XX:XX:XX:XX]", epilog="You can access the source codes at https://github.com/Bqrayvzdgn/Macchanger.")
    parser.add_argument("-i", "--interface", dest="interface", help="Enter your network interface")
    parser.add_argument("-m", "--mac_address", dest="mac_address", help="Enter your mac address")
    return parser.parse_args()

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

print("MyMacChanger started!")
(user_input,arguments) = get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
    print("Success!")
else:
    print("Error!")