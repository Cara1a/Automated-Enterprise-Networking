from netmiko import ConnectHandler

# for i in range(1, 7):
#     ios_l2 = {
#         "device_type": "cisco_ios",
#         "ip": "192.168.1." + str(100+i),
#         "username": "shawn",
#         "password": "cisco"
#     }
#     net_connect = ConnectHandler(**ios_l2)
#
#     print(ios_l2["ip"])
#     output = net_connect.send_command("show vlan bri")
#     print(output)

menu = [
    "1 - hello",
    "2 - there",
    "3 - general",
    "4 - kanobi",
    "5 - exit"
]

input = 0

def print_menu():
    for i in menu:
        print(i)

def get_switches():
    file = open("./switches.txt")

    switches = file.readlines()

    for switch in range(1, 10):

        print(switch)

print_menu()
get_switches()

