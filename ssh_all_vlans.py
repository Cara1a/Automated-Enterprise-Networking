from netmiko import ConnectHandler

ios_l2 = {
    "device_type": "cisco_ios",
    "ip": "",
    "username": "david",
    "password": "cisco"
}


IP_file = open("myswitch")

for IP in IP_file:
    IP = IP.strip()
    ios_l2["ip"] = IP
    ssh = ConnectHandler(**ios_l2)
    print("configuring " + IP)
    for n in range(2, 11):
        vlans_command = ["vlan " + str(n), "name SHAWN_VLAN_" + str(n)]
        output = ssh.send_config_set(vlans_command)
        print(output)

