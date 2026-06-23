#!/data/data/com.termux/files/usr/bin/python

import os
import subprocess
import re

def get_ip():
    try:
        output = subprocess.check_output(
            ["ifconfig"],
            text=True,
            stderr=subprocess.DEVNULL
        )

        ips = re.findall(r'inet\s+(\d+\.\d+\.\d+\.\d+)', output)

        for ip in ips:
            if not ip.startswith("127."):
                return ip



ip = get_ip()
print(ip)

    except Exception:
        pass

    return "Unknown"

print()
print("=" * 50)
print(" Phone To Server - Copyparty Setup")
print("=" * 50)
print(f"IP Address : {ip}")
print()

port = input("Enter port [8080]: ").strip()

if not port:
    port = "8080"

script_path = os.path.expanduser(
    "~/.config/copyparty/run-copyparty.sh"
)

os.makedirs(os.path.dirname(script_path), exist_ok=True)

with open(script_path, "w") as f:
    f.write(
f"""#!/data/data/com.termux/files/usr/bin/bash

copyparty -p {port} -v ~/storage/shared::r
"""
    )

os.chmod(script_path, 0o755)

print()
print("Created:")
print(script_path)
print()
print(f"Open in browser:")
print(f"http://{ip}:{port}")
print()
print("Starting Copyparty...")
print()

os.execvp(
    "bash",
    ["bash", script_path]
)
