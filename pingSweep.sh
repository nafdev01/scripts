#!/bin/bash
# This script will ping sweep a /24 network range and return the live hosts. It accepts two arguments, the first three octets of the IP address (mandatory) and the name of the output file. If the output file is not provided, the script will create a file called pingsweep-targets.txt in the current directory.

# Define some colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Check if IP address was provided
if [ "$#" -lt 1 ]; then
    echo -e "${RED}Usage: $0 <base IP> [output file]${NC}"
    echo -e "${RED}Example: $0 192.168.70 pingsweep-targets.txt${NC}"
    exit 1
fi

# Get the first three octets of the IP address from the user
ip_base=$1

# Get the output file name from the user, or use 'targets.txt' as a default
output_file=${2:-pingsweep-targets.txt}

# Empty the output file
# > $output_file

for octet in $(seq 1 254); do
    ip=$ip_base.$octet
    if ping -c 1 $ip &>/dev/null; then
        echo $ip | tee -a $output_file
    fi &
done
