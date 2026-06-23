#!/usr/bin/env python3

import subprocess
import re
import sys

def get_ip():
    try:
        output = subprocess.check_output(
            ["ifconfig"],
            text=True,
            stderr=subprocess.DEVNULL
        )

        # Find all IPv4 addresses
        ips = re.findall(r'inet\s+(\d+\.\d+\.\d+\.\d+)', output)

        # Skip localhost
        for ip in ips:
            if not ip.startswith("127."):
                return ip

        return None

    except Exception as e:
        print(f"Error getting IP: {e}")
        return None


def main():
    print("\n=== CopyParty Launcher ===\n")

    ip = get_ip()

    if not ip:
        print("Could not detect IP address.")
        sys.exit(1)

    print(f"Detected IP Address: {ip}")

    port = input("\nEnter port number [8080]: ").strip()

    if not port:
        port = "8080"

    print("\nStarting CopyParty...\n")
    print(f"URL: http://{ip}:{port}\n")

    cmd = [
        "copyparty",
        "-p",
        port,
        "-v",
        "~/storage/shared::r"
    ]

    subprocess.run(" ".join(cmd), shell=True)


if __name__ == "__main__":
    main()
