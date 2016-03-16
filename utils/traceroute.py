from scapy.all import *


__author__ = "Tobias Trabelsi"
__copyright__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Tobias Trabelsi"
__email__ = "Tobias.Trabelsi@HS-Bochum.de"
__status__ = "Testing"


def routeToHost(host):
    for i in range(1, 28):
        pkt = IP(dst=host, ttl=i) / UDP(dport=33434)
        reply = sr1(pkt, verbose=0)
        if reply is None:
            break
        elif reply.type == 3:
            print("Done!", reply.src)
            break
        else:
            print ("%d hops away: " % i, reply.src)
