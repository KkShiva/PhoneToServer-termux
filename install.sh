#!/data/data/com.termux/files/usr/bin/bash

set -e

APPDIR="$HOME/copyparty-android"

pkg update -y
pkg install -y python wget unzip net-tools

rm -rf "$APPDIR"

wget -O master.zip 
https://github.com/KkShiva/PhoneToServer-termux/archive/refs/heads/main.zip

unzip master.zip

mv copyparty-android-main "$APPDIR"

cd "$APPDIR"

pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Starting Web UI..."
echo ""

python server.py
