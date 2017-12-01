import socket;
import threading;
import sys;
import os;
import random;
import time;
from peerdiscover import PeerDiscover;
from peer import Peer;
from masterreceiver import MasterReceiver;
from messenger import Messenger;
from broadcaster import Broadcaster;
from queue import Queue, Empty;


IP_ADDRESS = "142.66.140";
PORT_MIN = 50000;
PORT_MAX = 50008;

def main():
	if len(sys.argv) != 2:
		print("Usage: {} [username]".format(sys.argv[0]));
		sys.exit(1);

    port = random.randint(PORT_MIN, PORT_MAX);
    try:
        socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    except:
        print('Could not create socket');
        exit(1);

	try:
		socket.bind(('', port)); 
	except:
        print('Could not bind socket');
        exit(1);

	
    hQueue = Queue();
    crQueue = Queue();
	csQueue = Queue();
    peerList = [];
	bc = Broadcaster(socket, peerList, sys.argv[1]);
	mr = MasterReceiver(socket, hQueue, crQueue);
    pd = PeerDiscover(socket, peerList, queue);
	mgr = Messenger(socket, peerList, crQueue, csQueue);
    
    pd.start();
	mr.start();
	pd.start();
	mgr.start();
	
	print("Loading peers...");
	time.sleep(5.0);
	
	msg = "";
	while True:
		if len(msg) == 1 && msg[0] == 'q':
			break;
		
		msg = input(sys.argv[1] + ": ");
		csqueue.put(msg);
	
	
main();
