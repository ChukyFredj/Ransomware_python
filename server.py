#! /usr/bin/python3

from cryptography.fernet import Fernet
import socket

key = Fernet.generate_key()
print("Votre clé est : ", key)

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",4321))
s.listen()

conn, addr = s.accept()
print(addr, "Connecté")

msg = conn.recv(2048).decode()
if msg == "key":
        conn.send(key)
        print("Key Send")
                           
