#!/data/data/com.termux/files/usr/bin/bash

echo "Updating packages..."
pkg update -y

echo "Installing requirements..."
pkg install -y git python unzip

WORKDIR="$HOME/PhoneToServer-termux"

echo "Cleaning old files..."
rm -rf "$WORKDIR"

echo "Cloning repository..."
git clone https://github.com/KkShiva/PhoneToServer-termux.git "$WORKDIR"

echo
echo "======================================"
echo "Installation Complete"
echo "======================================"
echo

echo "Project location:"
echo "$WORKDIR"
echo

echo "Files:"
ls -lah "$WORKDIR"

echo
echo "To run manually:"
echo

echo "cd $WORKDIR"
echo "python setup_copyparty.py"
echo
