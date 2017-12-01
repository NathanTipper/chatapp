import socket;
import threading;
import sys;
import os;
import random;
from peerdiscover import PeerDiscover;
from peer import Peer;
from masterreceiver from MasterReceiver;
from queue import Queue, Empty


IP_ADDRESS = "142.66.140";
PORT_MIN = 50000;
PORT_MAX = 50008;

def main():
    port = random.randint(PORT_MIN, PORT_MAX);
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    except:
        print('Could not create socket');
        exit(1);

    hQueue = Queue();
    cQueue = Queue();
    peerList = [];
    pd = PeerDiscover(socket, peerList, queue);
    
    pd.start();

main();
