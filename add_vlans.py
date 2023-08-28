import telnetlib
import getpass

IP_file = open("myswitches")
user = input("Enter your remote username: ")
password = getpass.getpass()

for IP in IP_file:
    IP = IP.strip()
    print("Configuring VLANs from " + IP)

    telnet = telnetlib.Telnet(IP)
    telnet.read_until(b"Username: ")
    telnet.write(user.encode('ascii') + b"\n")

    if password:
        telnet.read_until(b"Password: ")
        telnet.write(password.encode('ascii') + b"\n")

    telnet.write(b"conf t\n")
    for n in range(2, 21):
        telnet.write(b"vlan " + str(n).encode('ascii') + b"\n")
        telnet.write(b"name SHAWN_VLAN_" + str(n).encode('ascii') + b"\n")

    telnet.write(b"end\n")
    telnet.write(b"wr\n")
    telnet.write(b"exit\n")

    print(telnet.read_all().decode('ascii'))