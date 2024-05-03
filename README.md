# Cybersecurity Research and Study Scripts

This Git repository contains a collection of scripts that I use for my cybersecurity-related research and study. These scripts are designed to assist in various tasks such as network analysis, penetration testing, and exploring different security concepts. 

## Files

The repository consists of the following files:

- `arpDetector.py`: This script detects Address Resolution Protocol (ARP) spoofing attacks within a local network.
- `arpSpoofer.py`: This script enables ARP spoofing, allowing the manipulation of ARP tables to intercept network traffic.
- `cleanup_targets.py`: This script collects and cleans up lists of target IP addresses from a specified files.
- `echoClient.py`: This script implements a simple client for testing echo server functionality.
- `echoServer.py`: This script sets up an echo server that echoes back any message received from the client.
- `get_hosts_xml.py`: This is a script that extracts IP addresses found during an nmap host discovery scan from an XML file.
- `get_rmi_targets.sh`: # This is a bash script that parses through an nmap gnmap file that contains the results of a modiifed pingsweep done by aggressively scanning common rmi ports and returns the live hosts.
- `inPath.sh` - This is a bash script that checks if a specified command is in the PATH environment variable.
- `pingSweep.sh`: This is a bash script that performs a fast and simple ping sweep on a specified /24 subnet.
- `pysharktest.py`: This script demonstrates the usage of PyShark, a Python wrapper for the Wireshark network analysis tool.

## Usage

Each script is designed to be run independently, and they have specific use cases. Before running any script, please ensure that you have the necessary dependencies installed and configured properly. Detailed instructions for running each script can be found within their respective files as comments or in the accompanying documentation.


Happy scripting and stay secure!

