# Persians: Sydney Anderson, Tram Doan, Devon Knudsen, Zackary Phillips, Promyse Ward, James Wilson
# GitHub Repo URL: https://github.com/devonknudsen/Timing-Covert-Channel
# Written in Python 3.7

import socket
from sys import stdout
from time import time

DEBUG = True

# set the server's IP address and port
IP = "jeangourd.com"
PORT = 31337

# set time interval to binary equivalent
ONE = 0.1
ZERO = 0.025

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
s.connect((IP, PORT))

# recieve initial piece of data
data = s.recv(4096).decode()

# recieve data until EOF
covert_bin = ""
while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    delta = round(t1 - t0, 3)
    
    # display times between letters
    if(DEBUG):
        stdout.write("\tTime: \t" + str(delta) + "\n")
        stdout.flush()
        
    if (delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"
    

# close the connection to the server
s.close()

if(DEBUG):
    print("Binary received: " + str(covert_bin))
    print("\nConvert 8 byte binary to character:")

covert = ""
i = 0
while (i < len(covert_bin)):
    
    # b = a byte within the covert binary string 
    b = covert_bin[i:i+8]

    # break if there isn't an entire byte left
    if(len(b) != 8):
        break
    
    # convert the current byte (b) to its decimal value
    n = int("0b{}".format(b), 2)
    try:
        if(DEBUG):
            print("byte:\t" + str(b))
            print("int conversion: " + str(n))
            print("char conversion:\t" + chr(n) + "\n")
        
        # convert current decimal value (n) to equivalent character
        covert += chr(n)
        
    except:
        covert += "?"
        
    i += 8

# displays covert message
print("\nCovert message: " + covert)
