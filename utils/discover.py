import nmap
import sys


def discoverNetwork(ip):
    try:
        scanner = nmap.PortScanner();
        scanner.scan(hosts=ip, arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
        for host, status in hosts_list:
            print('{0}:{1}'.format(host, status))
        return hosts_list
    except nmap.PortScannerError:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(1)