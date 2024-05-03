import pyshark

# Create a capture object, specifying the network interface
capture = pyshark.LiveCapture(interface="eth0")

# Start capturing packets
capture.sniff()

# Loop through captured packets
for packet in capture:
    # Print the packet details
    print(packet)
