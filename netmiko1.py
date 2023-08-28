# from ssh import ConnectHandler
#
# iosv_l2 = {
#     'device_type': 'cisco_ios',
#     'ip': '192.168.122.72',
#     'username': 'david',
#     'password': 'cisco'
# }
#
# net_connect = ConnectHandler(**iosv_l2)
# output = net_connect.send_command('show ip int brief')
# print (output)
#
# config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
# output = net_connect.send_config_set(config_commands)
# print (output)
#
# for n in range (2,21):
#     print ("Creating VLAN " + str(n))
#     config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
#     output = net_connect.send_config_set(config_commands)
#     print (output)

from netmiko import ConnectHandler

ios_l2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "shawn",
    "password": "cisco"
}

ssh = ConnectHandler(**ios_l2)
output = ssh.send_command("show ip int bri")
print(output)

loop_back_commands = ["int loop 0", "ip addr 1.1.1.1 255.255.255.255"]
output = ssh.send_config_set(loop_back_commands)
print(output)
