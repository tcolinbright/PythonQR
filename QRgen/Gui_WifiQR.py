import qrcode
import tkinter as tk

# Define the Tkinter window
root = tk.Tk()
root.title("WiFi QR Code Generator")

# Define the WiFi security types
security_types = ["WEP", "WPA/WPA2", "Open"]

# Define the function to generate the QR code
def generate_qr():
    # Get the user input values
    ssid = ssid_entry.get()
    password = password_entry.get()
    security = security_var.get()
    
    # Generate the QR code with the network parameters
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(f"WIFI:T:{security};S:{ssid};P:{password};;")
    qr.make(fit=True)

    # Save the QR code as a PNG file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("wifi_qr.png")

# Define the label and entry widgets for the SSID
ssid_label = tk.Label(root, text="SSID:", width=45)
ssid_label.pack()

ssid_entry = tk.Entry(root)
ssid_entry.pack()

# Define the label and entry widgets for the password
password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Define the label and dropdown widget for the security type
security_label = tk.Label(root, text="Security:")
security_label.pack()

security_var = tk.StringVar(root)
security_var.set(security_types[1])
security_dropdown = tk.OptionMenu(root, security_var, *security_types)
security_dropdown.pack()

# Define the button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

# Start the Tkinter event loop
root.mainloop()

