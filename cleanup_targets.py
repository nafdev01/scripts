#!/usr/bin/env python3
"""
This is a script that reads a list of files and extracts unique IP addresses from them.
"""
import argparse


def get_unique_targets(file_list):
    ip_set = set()
    for file_name in file_list:
        with open(file_name, "r") as file:
            for line in file:
                ip_set.add(line.strip())
    return list(ip_set)


def get_args():
    parser = argparse.ArgumentParser(description="Get unique IP addresses from files.")
    parser.add_argument(
        "files",
        metavar="F",
        type=str,
        nargs="+",
        help="a list of files containing IP addresses",
        required=True,
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()

    unique_ips = get_unique_targets(args.files)
    print(unique_ips)
