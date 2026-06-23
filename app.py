#!/usr/bin/env python3

import subprocess
import re
import sys
import os

def get_ip():
"""
Get first non-local IPv4 address.
"""
try:
output = subprocess.check_output(
["ifconfig"],
text=True,
stderr=subprocess.DEVNULL
)

```
    ips = re.findall(
        r'inet\s+(\d+\.\d+\.\d+\.\d+)',
        output
    )

    for ip in ips:
        if not ip.startswith("127."):
            return ip

    return None

except Exception as e:
    print(f"Error detecting IP: {e}")
    return None
```

def select_share_folder():
"""
Choose folder to share.
"""
print("\nSelect Share Location")
print("---------------------")
print("1. Use /storage/shared")
print("2. Choose using Android File Picker")

```
choice = input("\nChoice [1]: ").strip()

if choice == "" or choice == "1":
    return "/storage/shared"

if choice == "2":
    try:
        print("\nChoose any file inside the folder you want to share...\n")

        picked_file = subprocess.check_output(
            ["termux-file-picker"],
            text=True
        ).strip()

        if not picked_file:
            print("No file selected.")
            sys.exit(0)

        folder = os.path.dirname(picked_file)

        print(f"\nSelected Folder:")
        print(folder)

        return folder

    except FileNotFoundError:
        print(
            "\ntermux-file-picker not found.\n"
            "Install Termux API:\n"
            "pkg install termux-api"
        )
        sys.exit(1)

    except Exception as e:
        print(f"\nError selecting folder: {e}")
        sys.exit(1)

print("\nInvalid selection.")
sys.exit(1)
```

def main():

```
print("\n==========================")
print("   CopyParty Launcher")
print("==========================\n")

ip = get_ip()

if not ip:
    print("Could not detect network IP.")
    sys.exit(1)

print(f"Detected IP : {ip}")

share_dir = select_share_folder()

port = input("\nEnter Port [8080]: ").strip()

if not port:
    port = "8080"

print("\n==========================")
print("Starting CopyParty")
print("==========================")

print(f"\nShared Folder : {share_dir}")
print(f"Port          : {port}")
print(f"URL           : http://{ip}:{port}")
print("\nPress CTRL+C to stop.\n")

cmd = [
    "copyparty",
    "-p",
    port,
    "-v",
    f"{share_dir}::r"
]

subprocess.run(cmd)
```

if **name** == "**main**":
main()
