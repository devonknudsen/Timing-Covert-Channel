import socket
from time import sleep
from binascii import hexlify

port = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))


covert = "secret" + "EOF"
print("Covert message: " + covert)
covert_bin = ""
for i in covert:
    covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)
print("Covert in binary: " + str(covert_bin))
n = 0
zero = 0.025
one = 0.1
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
for i in range(len(covert)):
    j = i
    if j > len(msg):
        j = i - len(msg)
    c.send(msg[j])
    if(covert_bin[n] == "0"):
        sleep(zero)
        print("Zero: \t" + str(zero))
        bin += "0"
    else:
        sleep(one)
        print("One: \t" + str(one))
        bin += "1"
    n = (n+1)%len(covert_bin)

c.send("EOF")
c.close()
print("Binary sent: " + str(bin))
