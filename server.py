import socket
from time import sleep
from binascii import hexlify

ZERO = 0.025
ONE = 0.1
PORT = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))


covert = "secret" + "EOF"
print("Covert message: " + covert)
covert_bin = ""
for i in covert:
    covert_bin += bin(int(hexlify(i.encode()), 16))[2:].zfill(8)
    
print("Covert in binary: " + covert_bin)
n = 0
bin = ""

# listens for clients
# this is a blocking call
s.listen(0)

# a client has connected!
c,addr = s.accept()

# set the message
msg = "Some message..."

# send the message, one letter at a time
print("Sending characters with delays:")
n = 0
count = 0
while(count < len(covert_bin)):
    for i in msg:
        c.send(i.encode())
        if (covert_bin[n] == "0"):
            sleep(ZERO)
        else:
            sleep(ONE)
        n = (n + 1) % len(covert_bin)
        count += 1
        
c.send("EOF".encode())
c.close()

print("Binary sent: " + str(bin))
