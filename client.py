import socket
from sys import stdout
from time import time

# set the server's IP address and port
ip = "localhost"
port = 1337
ONE = 0.1
ZERO= 0.025
covert_bin = ""

# create the socker
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
s.connect((ip, port))

# recieve data until EOF
data = s.recv(4096).decode().rstrip("\n")

print("Received characters with delays:")

while (data != "EOF"):
    stdout.write(str(data))
    stdout.flush()
    t0 = time()
    data = s.recv(4096).decode().rstrip("\n")
    t1 = time()
    delta = round(t1 - t0, 3)
    if (delta > ZERO):
        print("\tOne: \t" + str(delta))
        covert_bin += "1"
    else:
        print("\tZero: \t" + str(delta))
        covert_bin += "0"

print("Binary received: " + str(covert_bin))
question = input("Do you wish to show hidden msg? Y/N\n")
if (question.upper() == 'N'):
    print("Goodbye")
    exit()
print("\nConvert 8 byte binary to character:")
# close the connection to the server
s.close()

covert = ""
i = 0
while (i < len(covert_bin)):
    b = covert_bin[i:i+8]
    print("bytes: \t" + str(b))
    n = int("0b{}".format(b),2)
    print("int: " + str(n))
    try:
        covert += chr(n)
        print("char: \t" + chr(n))
    except:
        covert += "?"
    i += 8
    print("")
print("Covert message: " + covert)
