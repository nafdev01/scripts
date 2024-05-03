#!/usr/bin/env python3
"""
This is a script that extracts IP addresses found during an nmap host discovery scan from an XML file and writes them to a file.
"""
import argparse
import re
import xml.etree.ElementTree as ET

from termcolor import colored


def find_ips(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = ET.tostring(root, encoding="utf8").decode("utf8")

    # Find IP addresses in the XML data and return ip
    ip_pattern = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    ips = re.findall(ip_pattern, data)
    return ips


# write a list of ips to a file in append mode
def write_ips(filename, ips):
    with open(filename, "a") as f:
        for ip in ips:
            f.write(ip + "\n")
            print(colored(f" [+] {ip}", "green"))


def get_args():
    parser = argparse.ArgumentParser(description="Find IP addresses in an XML file.")
    parser.add_argument("-i", "--input", help="The XML file to search", required=True)
    parser.add_argument(
        "-o", "--output", help="The output file to write the IP addresses to"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()

    found_ips = find_ips(args.input)
    if len(found_ips) > 0:
        if args.output:
            print(
                colored(f" [+] Writing {len(found_ips)} IPs to {args.output}", "yellow")
            )
            write_ips(args.output, found_ips)
        else:
            print(colored("IPs found:", "green"))
            for ip in found_ips:
                print(colored(f" [+] {ip}", "green"))
    else:
        print(colored(f" [!!] No IPs found in {args.input}", "red"))

    exit()
