from utils import discover, scanner, ssh
import os
import sys

__author__ = "Tobias Trabelsi"
__copyright__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Tobias Trabelsi"
__email__ = "Tobias.Trabelsi@HS-Bochum.de"
__status__ = "Testing"

if __name__ == '__main__':
    euid = os.geteuid()
    if euid != 0:
        print ("Script not started as root. Running sudo..")
        args = ['sudo', sys.executable] + sys.argv + [os.environ]
        # the next line replaces the currently-running process with the sudo
        os.execlpe('sudo', *args)

    hostlist = discover.discoverNetwork('192.168.0.1/24')
    for host in hostlist:
        scanner.scanhost(host[0], '0-1000')
    print(scanner.getMacForHost('192.168.0.1'))
    ssh.connectToHost("192.168.0.211")
