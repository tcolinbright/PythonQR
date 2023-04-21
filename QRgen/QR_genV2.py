import tkinter as tk
import qrcode
from PIL import Image
from tkinter import filedialog

def generate_qr(event=None):
    # Get the user input from the GUI
    data = entry.get()

    # Create the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Open a file dialog box to get the file name and location
    file_path = filedialog.asksaveasfilename(defaultextension='.png')

    # Save the QR code image as a .png to the chosen file path
    img.save(file_path)

# Create the GUI window
root = tk.Tk()
root.title("QR Code Generator")

# Create label and entry widgets
label = tk.Label(root, text="Enter QR Contents:")
label.pack()

# Create the input field
entry = tk.Entry(root, width=55)
entry.pack()

# Create the generate button and bind the return key to it
button = tk.Button(root, text="Generate", command=generate_qr)
button.pack()
root.bind('<Return>', generate_qr)

# Start the GUI loop
root.mainloop()

