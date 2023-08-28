from netmiko import ConnectHandler

for i in range(1, 7):
    ios_l2 = {
        "device_type": "cisco_ios",
        "ip": "192.168.1." + str(100+i),
        "username": "shawn",
        "password": "cisco"
    }
    net_connect = ConnectHandler(**ios_l2)

    output = net_connect.send_command("show ip int bri")
    print(output)

    output = net_connect.send_command("show vlan bri")
    print(output)

    remove_vlan_commands = ["no vlan 2-99"]

    output = net_connect.send_config_set(remove_vlan_commands)
    print(output)

    output = net_connect.send_command("show vlan bri")
    print(output)

