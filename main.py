from utils import discover, scanner
import os
import sys

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