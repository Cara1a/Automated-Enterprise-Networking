import telnetlib
import getpass

# initialization
IP_file = open("myswitches")
user = input("enter your remote username: ")
password = getpass.getpass()

for IP in IP_file:
    IP = IP.strip()
    print("Configuring SSH from " + IP)
    telnet = telnetlib.Telnet(IP)
    telnet.read_until(b"Username: ")
    telnet.write(user.encode('ascii') + b"\n")

    if password:
        telnet.read_until(b"Password: ")
        telnet.write(password.encode('ascii') + b"\n")

    telnet.write(b"conf t\n")
    telnet.write(b"username david priv 15\n")
    telnet.write(b"line vty 0 15\n")
    telnet.write(b"login local\n")
    telnet.write(b"transport input all\n")
    telnet.write(b"exit\n")
    telnet.write(b"ip domain-name cciepython.com\n")
    telnet.write(b"crypto key generate rsa\n")
    telnet.write(b"1024\n")

    telnet.write(b"end\n")
    telnet.write(b"wr\n")
    telnet.write(b"exit\n")
    print(telnet.read_all().decode('ascii'))