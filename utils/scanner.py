import sys
import nmap
import os

__author__ = "Tobias Trabelsi"
__copyright__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Tobias Trabelsi"
__email__ = "Tobias.Trabelsi@HS-Bochum.de"
__status__ = "Testing"


def scanhost (ip, range):
    try:
        scanner = nmap.PortScanner();
        scanner.scan(ip, range)
        print("Start Scanning...")
        for host in scanner.all_hosts():
            print('----------------------------------------------------')
            print('Host : {0} ({1})'.format(host, scanner[host].hostname()))
            print('State : {0}'.format(scanner[host].state()))

            for proto in scanner[host].all_protocols():
                print('----------')
                print('Protocol : {0}'.format(proto))

                lport = list(scanner[host][proto].keys())
                lport.sort()
                for port in lport:
                    print('port : {0}\tstate : {1}'.format(port, scanner[host][proto][port]))

    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(1)


def getMacForHost(host):
    try:
        euid = os.geteuid()
        if euid != 0:
            print ("Script not started as root. Running sudo..")
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            os.execlpe('sudo', *args)

        scanner = nmap.PortScanner();
        print('scanning ' + host)
        scanner.scan(host, arguments='-O')
        for h in scanner.all_hosts():
            if 'mac' in scanner[h]['addresses']:
                print(scanner[h]['addresses'], scanner[h]['vendor'])
                return scanner[h]['addresses']['mac']
    except nmap.PortScannerError:
        print("This function requires root privileges")
        sys.exit(1)