#!/usr/bin/env python3

import os
import re
import subprocess
import sys


def get_ip():
    try:
        output = subprocess.check_output(
            ["ifconfig"], text=True, stderr=subprocess.DEVNULL
        )

        ips = re.findall(r"inet\s+(\d+\.\d+\.\d+\.\d+)", output)

        for ip in ips:
            if not ip.startswith("127."):
                return ip

        return None

    except Exception as e:
        print(f"Error detecting IP: {e}")
        return None


def select_share_folder():
    print("\nShare Location")
    print("--------------")
    print("1. Share entire Internal Storage (/storage/shared)")
    print("2. Pick a file from desired folder")

    choice = input("\nChoice: ").strip()

    if choice == "" or choice == "1":
        return "/storage/shared"

    if choice == "2":
        try:
            print("\nAndroid file picker will open.")
            print("Select ANY file inside the folder you want to share.\n")

            selected_file = subprocess.check_output(
                ["termux-file-picker"], text=True
            ).strip()

            if not selected_file:
                print("No file selected.")
                sys.exit(0)

            folder = os.path.dirname(selected_file)

            print(f"\nSelected File:")
            print(selected_file)

            print(f"\nSharing Folder:")
            print(folder)

            return folder

        except FileNotFoundError:
            print("\ntermux-file-picker not found.")
            print("Install with:")
            print("pkg install termux-api")
            sys.exit(1)

        except Exception as e:
            print(f"\nError: {e}")
            sys.exit(1)

    print("Invalid selection.")
    sys.exit(1)


def main():
    print("\n========================")
    print("   PhoneToServer")
    print("========================")

    ip = get_ip()

    if not ip:
        print("Unable to detect IP address.")
        sys.exit(1)

    print(f"\nDetected IP : {ip}")

    share_dir = select_share_folder()

    port = input("\nEnter Port: ").strip()

    if not port:
        port = "8080"

    print("\n========================")
    print("Starting CopyParty")
    print("========================")

    print(f"\nFolder : {share_dir}")
    print(f"Port   : {port}")
    print(f"URL    : http://{ip}:{port}")

    cmd = ["copyparty", "-p", port, "-v", f"{share_dir}::r"]

    print("\nPress CTRL+C to stop.\n")

    subprocess.run(cmd)


if __name__ == "__main__":
    main()
