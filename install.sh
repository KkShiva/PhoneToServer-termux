#!/data/data/com.termux/files/usr/bin/bash

echo "Updating packages..."
pkg update -y

echo "Installing Python..."
pkg install -y python
pkg install net-tools

echo "Installing Copyparty..."
pip install --upgrade pip
pip install --upgrade copyparty




mkdir -p ~/.config/copyparty

cat > ~/.config/copyparty/start.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash

copyparty -p 8080 -v ~/storage/shared::r
EOF

chmod +x ~/.config/copyparty/start.sh




ifconfig
copyparty -p 8080 -v ~/storage/shared::r
