import qrcode

# Define the WiFi network parameters
network = {
    "ssid": "MyWiFiNetwork",
    "password": "MyWiFiPassword",
    "security": "WPA/WPA2"
}

# Generate the QR code with the network parameters
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(f"WIFI:T:{network['security']};S:{network['ssid']};P:{network['password']};;")
qr.make(fit=True)

# Save the QR code as a PNG file
img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_qr.png")

