from wakeonlan import wol

__author__ = "Tobias Trabelsi"
__copyright__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Tobias Trabelsi"
__email__ = "Tobias.Trabelsi@HS-Bochum.de"
__status__ = "Testing"


def wakeHost(hostMacAddresse):
    wol.send_magic_packet(hostMacAddresse)