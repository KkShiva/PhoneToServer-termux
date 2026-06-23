#!/data/data/com.termux/files/usr/bin/python

import os
import re
import subprocess
import sys

def get_ips():
try:
output = subprocess.check_output(
["ifconfig"],
stderr=subprocess.STDOUT
).decode()

```
    ips = re.findall(
        r"inet\s+(\d+\.\d+\.\d+\.\d+)",
        output
    )

    return [
        ip for ip in ips
        if not ip.startswith("127.")
    ]

except Exception:
    return []
```

def choose_folder():
default = os.path.expanduser("~/storage/shared")

```
print("\nFolder to share")
print(f"Default: {default}")

folder = input(
    "Enter path (blank for default): "
).strip()

if not folder:
    folder = default

return os.path.expanduser(folder)
```

def choose_port():
port = input(
"\nPort [8080]: "
).strip()

```
if not port:
    port = "8080"

return port
```

def main():

```
print("=" * 60)
print(" PhoneToServer-Termux ")
print("=" * 60)

ips = get_ips()

print("\nDetected IP Addresses:\n")

for ip in ips:
    print(f"  {ip}")

folder = choose_folder()
port = choose_port()

print("\nStarting Copyparty...\n")

for ip in ips:
    print(f"  http://{ip}:{port}")

print(f"\nSharing: {folder}\n")

cmd = [
    "copyparty",
    "-p",
    str(port),
    "-v",
    f"{folder}::r"
]

os.execvp(cmd[0], cmd)
```

if **name** == "**main**":
main()
