#!/data/data/com.termux/files/usr/bin/bash

echo "Updating packages..."
pkg update -y

echo "Installing Python..."
pkg install -y python

echo "Installing Copyparty..."
pip install --upgrade pip
pip install --upgrade copyparty

echo ""
echo "Grant storage permission if not already done:"
echo ""
echo "    termux-setup-storage"
echo ""

mkdir -p ~/.config/copyparty

cat > ~/.config/copyparty/start.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash

copyparty -p 8080 -v ~/storage/shared::r
EOF

chmod +x ~/.config/copyparty/start.sh

echo ""
echo "Installation complete."
echo ""
echo "Start server with:"
echo ""
echo "    ~/.config/copyparty/start.sh"
echo ""
echo "Then open:"
echo ""
echo "    http://PHONE-IP:8060"
echo ""