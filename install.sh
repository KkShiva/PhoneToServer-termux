#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "Updating packages..."
pkg update -y

echo "Installing dependencies..."
pkg install -y python net-tools termux-api

echo "Grant storage access..."
termux-setup-storage

echo "Installing Copyparty..."
python -m pip install --upgrade pip
python -m pip install --upgrade copyparty

mkdir -p ~/PhoneToServer

curl -L 
https://raw.githubusercontent.com/KkShiva/PhoneToServer-termux/main/app.py 
-o ~/PhoneToServer/app.py

chmod +x ~/PhoneToServer/app.py

echo ""
echo "Installation completed."
echo ""
echo "Run:"
echo "python ~/PhoneToServer/app.py"
