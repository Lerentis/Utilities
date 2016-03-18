from wakeonlan import wol
import sys

__author__ = "Tobias Trabelsi"
__copyright__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Tobias Trabelsi"
__email__ = "Tobias.Trabelsi@HS-Bochum.de"
__status__ = "Testing"


def wakeHost(hostMacAddresse):
    try:
        wol.send_magic_packet(hostMacAddresse)
    except:
        print("No Connection to host or no MAC Addresse receaved")
        print(sys.exc_info()[0])