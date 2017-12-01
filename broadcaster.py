from threading import Thread, Timer;
from queue import Queue, Empty
import socket

IP_ADDRESS = "142.66.140."
C_MIN = 21;
C_MAX = 69;
D_MIN = 172;
PORT_MIN = 50000;
PORT_MAX = 50008;

class Broadcaster(Thread):
	def __init__(self, socket, peerlist, username):
                Thread.__init__(self);
                self.socket = socket;
                self.peerlist = peerlist;
                self.msg = "HELLO" + username;
		
	def run(self):
		self.initial_broadcast();
		timer = Timer(5.0, self.broadcast);
		timer.start();
		if(not timer.is_alive()):
                        timer = Timer(5.0, self.broadcast);
                        timer.start();
			
	def initial_broadcast(self):
                extension = C_MIN;
                encodedMessage = self.msg.encode();
                while extension <= D_MIN:
                        port = PORT_MIN;
                        while port <= PORT_MAX:
                                print("Sending initial HELLO msg to: " + IP_ADDRESS+str(extension) + " : " + str(port));
                                self.socket.sendto(encodedMessage, (IP_ADDRESS+str(extension), port));
                                port += 1;
			
                        extension += 1;
			
                        if(extension > C_MAX and extension < D_MIN):
                                extension = D_MIN;
				
	def broadcast(self):
                encodedMessage = self.msg.encode();
                print(encodedMessage);
                for i in range(0, len(self.peerlist)):
                        addr = self.peerlist[i].addr;
                        port = self.peerlist[i].port;
                        self.socket.sentto(encodedMessage, (addr, port));
