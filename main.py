from network import discover, scanner, ssh, traceroute, wol
from geometrics import geometric
import os
import sys

__author__ = "Tobias Trabelsi"
__copyright__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Tobias Trabelsi"
__email__ = "Tobias.Trabelsi@HS-Bochum.de"
__status__ = "Testing"

if __name__ == '__main__':
    geometric.calcCylinder(5.0,7.0)


    #euid = os.geteuid()
    #if euid != 0:
    #    print ("Script not started as root. Running sudo..")
    #    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    #    os.execlpe('sudo', *args)
#
#    hostlist = discover.discoverNetwork('192.168.1.1/24')
#    for host in hostlist:
#        scanner.scanhost(host[0], '0-1000')
#    wol.wakeHost(scanner.getMacForHost('192.168.1.1'))
#    ssh.connectToHost("PoolPC0.local")
#    traceroute.routeToHost("PoolPC0.local")