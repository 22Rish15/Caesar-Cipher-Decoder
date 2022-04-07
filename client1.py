from email import message
import socket

dec_key = input("Please give me encryption key: \n")

if len(dec_key) == 40 :
    s= socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    s.connect((socket.gethostname(),32120))
    message= s.recv(1000)
    message= message.decode("utf-8")

    val = dec_key[::-1];
    dec = dict(zip(val,dec_key))
    message = "".join([dec[words] for words in message])
    print(message)

else:
    print("You are not authorized for this info.")