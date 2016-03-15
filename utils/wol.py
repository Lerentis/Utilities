from wakeonlan import wol


def wakeHost(hostMacAddresse):
    wol.send_magic_packet(hostMacAddresse)