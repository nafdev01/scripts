#!/bin/bash
# This is a bash script that parses through an nmap gnmap file that contains the results of a modiifed pingsweep done by scanning common rmi ports and returns the live hosts. It accepts two arguments, the name of the nmap file (mandatory) and the name of the output file. If the output file is not provided, the script will create a file called rmi-targets.txt in the current directory.

# Example usage: ./get_rmi_targets.sh nmap-results.gnmap rmi-targets.txt

# Define some colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
YELLOW='\033[1;33m'

# Check if nmap file was provided
if [ "$#" -lt 1 ]; then
    echo -e "${RED}Usage: $0 <nmap file> [output file]${NC}"
    echo -e "${RED}Example: $0 nmap-results.gnmap rmi-targets.txt${NC}"
    exit 1
fi

# Get the nmap file name from the user
nmap_file=$1

# Check if output file was provided
if [ "$#" -eq 2 ]; then
    output_file=$2
else
    output_file="rmi-targets.txt"
fi

# Check if nmap file exists
if [ ! -f "$nmap_file" ]; then
    echo -e "${RED}Error: $nmap_file does not exist.${NC}"
    exit 1
fi

# Parse the nmap file and write the results to the output file
cat $nmap_file | grep open | cut -d " " -f2 >$output_file

echo -e "${GREEN}Parsing complete. Results written to $output_file.${NC}"
for ip in $(cat $output_file); do
    echo -e "${YELLOW} [+] $ip${NC}"
done
