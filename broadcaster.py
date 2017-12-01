from threading import Thread, Timer;
from queue import Queue, Empty
import socket

IP_ADDRESS = "142.66.140"
C_MIN = 21;
C_MAX = 69;
D_MIN = 186;
PORT_MIN = 50000;
PORT_MAX = 50008;

class Broadcaster(Thread):
	def __init__(self, socket, peerlist, username):
		self.socket = socket;
		self.msg = "HELLO" + username;
		self.username = username;
		
	def run():
		initial_broadcast();
		timer = Timer(5.0, broadcast);
		timer.start();
		if(!timer.is_alive())
			timer.start();
			
	def initial_broadcast():
		extension = C_MIN;
		while extension <= D_MIN
			port = PORT_MIN;
			while port <= PORT_MAX:
				self.socket.sendto(self.msg, (IP_ADDRESS+extension, port);
				port += 1;
			
			extension += 1;
			
			if(extension > C_MAX && extension < D_MIN)
				extension = D_MIN;
				
	def broadcast():
		for i in range(0, len(peerList)):
			addr = peerList[i].addr;
			port = peerList[i].port;
			self.socket.sentto(self.msg, (addr, port));