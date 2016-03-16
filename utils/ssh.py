import getpass
import socket
import sys
import traceback
from paramiko.py3compat import input

import paramiko
try:
    import interactive
except ImportError:
    from . import interactive


__author__ = "Tobias Trabelsi"
__copyright__ = "GPLv3"
__credits__ = ["Robey Pointer", "The Paramiko Project"]
__version__ = "1.0"
__maintainer__ = "Tobias Trabelsi"
__email__ = "Tobias.Trabelsi@HS-Bochum.de"
__status__ = "Testing"


def connectToHost(host):
    # Paramiko client configuration
    UseGSSAPI = True             # enable GSS-API / SSPI authentication
    DoGSSAPIKeyExchange = True
    port = 22

    # get hostname
    username = ''
    if len(host) > 1:
        hostname = host
        if hostname.find('@') >= 0:
            username, hostname = hostname.split('@')
    else:
        hostname = input('Hostname: ')
    if len(hostname) == 0:
        print('*** Hostname required.')
        sys.exit(1)

    if hostname.find(':') >= 0:
        hostname, portstr = hostname.split(':')
        port = int(portstr)

    # get username
    if username == '':
        default_username = getpass.getuser()
        username = input('Username [%s]: ' % default_username)
        if len(username) == 0:
            username = default_username
    if not UseGSSAPI or (not UseGSSAPI and not DoGSSAPIKeyExchange):
        password = getpass.getpass('Password for %s@%s: ' % (username, hostname))

    # now, connect and use paramiko Client to negotiate SSH2 across the connection
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        print('*** Connecting...')
        if not UseGSSAPI or (not UseGSSAPI and not DoGSSAPIKeyExchange):
            client.connect(hostname, port, username, password)
        else:
            # SSPI works only with the FQDN of the target host
            hostname = socket.getfqdn(hostname)
            try:
                client.connect(hostname, port, username, gss_auth=UseGSSAPI,
                               gss_kex=DoGSSAPIKeyExchange)
            except Exception:
                password = getpass.getpass('Password for %s@%s: ' % (username, hostname))
                client.connect(hostname, port, username, password)

        chan = client.invoke_shell()
        print(repr(client.get_transport()))
        print('*** Here we go!\n')
        interactive.interactive_shell(chan)
        chan.close()
        client.close()

    except Exception as e:
        print('*** Caught exception: %s: %s' % (e.__class__, e))
        traceback.print_exc()
        try:
            client.close()
        except:
            pass
        sys.exit(1)