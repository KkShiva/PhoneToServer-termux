#!/data/data/com.termux/files/usr/bin/bash

echo "Updating packages..."
pkg update -y

echo "Installing requirements..."
pkg install -y git python unzip

echo "Installing Copyparty..."
pip install --upgrade pip
pip install --upgrade copyparty

WORKDIR="$HOME/PhoneToServer-termux"

rm -rf "$WORKDIR"

echo "Downloading project..."
git clone https://github.com/KkShiva/PhoneToServer-termux.git "$WORKDIR"

cd "$WORKDIR" || exit 1

echo
echo "Running setup..."
python setup_copyparty.py
