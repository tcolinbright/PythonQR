# QRGen

This program generates a simple GUI window that allows the user to enter data and generate a QR code image from that data.

Here is a detailed walk-through of the code:

```python

import tkinter as tk
import qrcode
from PIL import Image
from tkinter import filedialog
```

This block of code imports the necessary modules for this program. ```tkinter``` is used to create the GUI window, ```qrcode``` is used to generate the QR code, ```PIL``` is used to create and save the QR code image as a PNG file, and ```filedialog``` is used to open a dialog box to allow the user to choose where to save the image file.


```python
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
```


This block of code defines the function ```generate_qr``` that generates the QR code image. When the function is called, it gets the user input from the GUI and uses that data to create the QR code. It then creates the QR code image, opens a file dialog box to allow the user to choose where to save the image file, and saves the QR code image as a PNG file to the chosen file path.


```python
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
```

This block of code creates the GUI window, including the title, label, input field, and generate button. It also binds the Return key to the ```generate_qr``` function so that the user can hit Enter to generate the QR code. Finally, it starts the GUI loop to display the window.


Overall, this program is a simple and useful tool for generating QR codes from user input in a graphical interface. The user can easily save the generated QR code as a PNG file for use in various applications.
