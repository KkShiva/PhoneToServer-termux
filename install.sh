#!/data/data/com.termux/files/usr/bin/bash

echo "Updating packages..."
pkg update -y

echo "Installing requirements..."
pkg install -y python unzip wget

echo "Installing Copyparty..."
pip install --upgrade pip
pip install --upgrade copyparty

WORKDIR="$HOME/PhoneToServer-termux"

rm -rf "$WORKDIR"
mkdir -p "$WORKDIR"

cd "$HOME" || exit 1

wget -O PhoneToServer-termux.zip 
https://github.com/KkShiva/PhoneToServer-termux/archive/refs/heads/main.zip

unzip -o PhoneToServer-termux.zip

cd PhoneToServer-termux-main || exit 1

python setup_copyparty.py
