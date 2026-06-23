#!/data/data/com.termux/files/usr/bin/bash
pkg update -y
pkg install -y python net-tools
pip install -r requirements.txt
python server.py
