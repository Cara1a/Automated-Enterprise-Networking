import telnetlib
import getpass

# initialization
IP_file = open("myswitches")
user = input("enter your remote username: ")
password = getpass.getpass()

for IP in IP_file:
    IP = IP.strip()
    print("add user shawn from " + IP)
    telnet = telnetlib.Telnet(IP)
    telnet.read_until(b"Username: ")
    telnet.write(user.encode('ascii') + b"\n")

    if password:
        telnet.read_until(b"Password: ")
        telnet.write(password.encode('ascii') + b"\n")

    telnet.write(b"username shawn privilege 15 password cisco\n")
    telnet.write(b"no username david\n\n")

    telnet.write(b"end\n")
    telnet.write(b"wr\n")
    telnet.write(b"exit\n")
    print(telnet.read_all().decode('ascii'))