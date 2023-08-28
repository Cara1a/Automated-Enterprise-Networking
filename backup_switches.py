import telnetlib
import getpass

IP_file = open("myswitches")
user = input("Enter your remote username: ")
password = getpass.getpass()

for IP in IP_file:
    IP = IP.strip()
    print("Get config file from " + IP + " switch")

    telnet = telnetlib.Telnet(IP)
    telnet.read_until(b"Username: ")
    telnet.write(user.encode('ascii') + b"\n")

    if password:
        telnet.read_until(b"Password: ")
        telnet.write(password.encode('ascii') + b"\n")

    telnet.write(b"terminal length 0\n")
    telnet.write(b"show run\n")
    telnet.write(b"exit\n")

    configOutput = telnet.read_all()
    switch_file = open("switch_config/switch_" + IP, "w")
    switch_file.write(configOutput.decode('ascii'))
    switch_file.write("\n")
    switch_file.close()
    print(telnet.read_all().decode('ascii'))