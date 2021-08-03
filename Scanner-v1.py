import socket
import os
import time


os.system("clear")
print("\033[1;31m")
os.system("figlet SCANNERv1")
print("\33[1;33m")
print("Coded By: Zoro")
print("""\033[1;35m
==============================
=      CTRL + C TO EXIT      =
========-------------=========
""")
ip = raw_input("\033[1;37mIP: Alvo: ")
for porta in range(1, 65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((ip, porta)) == 0:
		print("PORTA: => {} [ABERTA!!]".format(porta))
		s.close()
