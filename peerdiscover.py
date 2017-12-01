from peer import Peer;
from queue import Queue, Empty;
from threading import Thread, Timer;

class PeerDiscover(Thread):
    def __init__(self, peerlist, queue, bufflen = 1024):
        self.peerlist = peerlist;
        self.queue = queue;
        self.bufflen = bufflen;
        self.timers = [];

    def run():
        while True:
            try:
                msg, addr = self.queue.get(False);
                newPeer = peer(msg, addr[0], addr[1]); # Create a new peer based on the username, which is given by the text before a semicolon, and the address.
                exists = existInList(newPeer); # If the peer exists, an index is returned. Otherwise, -1 is returned and we need to add the peer.
                if exists < 0:
                    peerList.append(newPeer);
                    print(newPeer.username + " has come online."
                    timers.append(Timer(15.0, self.delete_peer, len(timers)));
                    timers(-1).start();
                else:
                    try:
                        timers[exists].cancel(); # If the peer already exists, cancel the current timer
                        timers[exists] = Timer(15.0, self.delete_peer, exists); # and start a new one
                        timers[exists].start();
                    except:
                        print('Could not delete and add new Timer');
            except Queue.Empty:
                # do nothing

    def delete_peer(index):
        try:
            del timers[index];
            print(peerList[index] + " has gone offline.");
            del peerList[index];
        except:
            print('Cannot delete index of lists');

    def existInList(peer):
        for i in range(0, len(peerlist)):
            if peerlist[i].areEqual(peer):
                return i;

        return -1;
