import socket
from sys import stdout
from time import time

DEBUG = True

# set the server's IP address and port
IP = "localhost"
PORT = 1337

# set time interval to binary equivalent
ONE = 0.1
ZERO = 0.025
covert_bin = ""

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
s.connect((IP, PORT))

# recieve initial piece of data
data = s.recv(4096).decode()

# recieve data until EOF
while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    delta = round(t1 - t0, 3)
    if (delta >= ONE):
        if(DEBUG):
            stdout.write("\tOne: \t" + str(delta) + "\n")
        covert_bin += "1"
    else:
        if(DEBUG):
            stdout.write("\tZero: \t" + str(delta) + "\n")
        covert_bin += "0"
    
    stdout.flush()

# close the connection to the server
s.close()

if(DEBUG):
    print("Binary received: " + str(covert_bin))
    print("\nConvert 8 byte binary to character:")

covert = ""
i = 0
while (i < len(covert_bin)):
    b = covert_bin[i:i+8]

    # break if there isn't an entire byte
    if(len(b) != 8):
        break

    if(DEBUG):
        print("bytes: \t" + str(b))
    n = int("0b{}".format(b),2)
    if(DEBUG):
        print("int: " + str(n))
    try:
        covert += chr(n)
        if(DEBUG):
            print("char: \t" + chr(n))
    except:
        covert += "?"
        
    i += 8

print("Covert message: " + covert)
