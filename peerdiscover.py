from peer import Peer;
from queue import Queue, Empty;
from threading import Thread, Timer;
import time;

class PeerDiscover(Thread):
    def __init__(self, peerlist, hQueue, bufflen = 1024):
        Thread.__init__(self);
        self.peerlist = peerlist;
        self.hQueue = hQueue;
        self.bufflen = bufflen;
        self.timers = [];

    def run(self):
        while True:
            try:
                msg, addr = self.hQueue.get(False);
                newPeer = Peer(msg, addr[0], addr[1]); # Create a new peer based on the username, which is given by the text before a semicolon, and the address.
                exists = self.existInList(newPeer); # If the peer exists, an index is returned. Otherwise, -1 is returned and we need to add the peer.
                if exists == 0:
                    continue;
                elif exists < 0:
                    self.peerlist.append(newPeer);
                    print("\n" + newPeer.username + " has come online.");
                    self.timers.append(Timer(15.0, self.delete_peer, [newPeer]));
                    self.timers[-1].start();
                else:
                    try:
                        self.timers[exists-1].cancel(); # If the peer already exists, cancel the current timer
                        self.timers[exists-1] = Timer(15.0, self.delete_peer, [newPeer]); # and start a new one
                        self.timers[exists-1].start();
                    except IndexError as ie:
                        print(ie);
            except Empty:
                continue;
            
    def delete_peer(self,peer):
        index = self.existInList(peer);
        print(self.peerlist[index].username + " has gone offline.");
        try:
            del self.peerlist[index];
        except:
            print('Cannot delete peer from list');

    def existInList(self, peer):
        for i in range(0, len(self.peerlist)):
            if self.peerlist[i].areEqual(peer):
                return i;

        return -1;
