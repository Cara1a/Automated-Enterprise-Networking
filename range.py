import telnetlib
import getpass

HOST = "192.168.122.72"
user = input("Enter your User Name: ")
password = getpass.getpass()

telnet = telnetlib.Telnet(HOST)

telnet.read_until(b"Username: ")
telnet.write(user.encode('ascii') + b"\n")

if password:
    telnet.read_until(b"Password: ")
    telnet.write(password.encode('ascii') + b"\n")

telnet.write(b"enable\n")
telnet.write(b"cisco\n")
telnet.write(b"conf t\n")

# loopback address
telnet.write(b"int loopback 0\n")
telnet.write(b"ip addr 1.1.1.1 255.255.255.255\n")
telnet.write(b"int loopback 1\n")
telnet.write(b"ip addr 2.2.2.2 255.255.255.255\n")
telnet.write(b"exit\n")

# vlan range
for n in range(2, 11):
    telnet.write(b"vlan " + str(n).encode('ascii') + b"\n")
    telnet.write(b"name shawn_VLAN_" + str(n).encode('ascii') + b"\n")

telnet.write(b"exit\n")
telnet.write(b"wr\n")
telnet.write(b"end\n")

print(telnet.read_all().decode('ascii'))
