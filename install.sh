#!/data/data/com.termux/files/usr/bin/bash

pkg update -y
pkg install -y python net-tools

pip install --upgrade pip
pip install --upgrade copyparty

mkdir -p ~/.config/copyparty

python3 setup_copyparty.py
