#!/data/data/com.termux/files/usr/bin/bash

echo "Updating packages..."
pkg update -y

echo "Installing Python..."
pkg install -y python net-tools

echo "Installing Copyparty..."
pip install --upgrade pip
pip install --upgrade copyparty

mkdir -p ~/.config/copyparty

echo
echo "========================================"
echo "Network Information"
echo "========================================"
ifconfig
echo

echo
printf "Enter Copyparty port [8080]: "
read PORT

[ -z "$PORT" ] && PORT=8080

echo "Selected port: $PORT"

cat > ~/.config/copyparty/run-copyparty.sh << EOF
#!/data/data/com.termux/files/usr/bin/bash

copyparty -p $PORT -v ~/storage/shared::r
EOF

chmod +x ~/.config/copyparty/run-copyparty.sh

echo
echo "Starting Copyparty on port $PORT ..."
echo

~/.config/copyparty/run-copyparty.sh
