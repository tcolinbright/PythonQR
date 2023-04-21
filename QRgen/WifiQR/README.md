# WiFi QR Code Generator

The "WiFi QR Code Generator" is a Python program that generates a QR code for a WiFi network based on user input. The program uses the qrcode library to generate the QR code and the tkinter library to create a graphical user interface (GUI) for the program.
Installation

To install the "WiFi QR Code Generator", follow these steps:

1. Install Python 3.x on your computer if it is not already installed.
1. Open a command prompt or terminal window and navigate to the directory where you want to install the program.

1. Install the required libraries using pip:

```bash
pip install qrcode pillow
```

## Usage

To use the "WiFi QR Code Generator", follow these steps:

1. Open a command prompt or terminal window and navigate to the directory where the program is installed.
1. Run the program using the following command:

```bash
python Gui_WifiQR.py
```
- The program window will open, prompting you to enter the SSID, password, and security type for the WiFi network you want to generate a QR code for.
- Select the security type from the dropdown menu.
- Click the "Generate QR Code" button.
- The QR code will be generated and saved as a PNG file in the same directory as the program.

<br><br/>

## Code Breakdown

```python
# Import the necessary libraries
import qrcode
import tkinter as tk

# Define the Tkinter window
root = tk.Tk()
root.title("WiFi QR Code Generator")
```

The code starts by importing the necessary libraries: ```qrcode``` for generating QR codes and ```tkinter``` for creating the GUI. Then, it defines the root object as a ```Tkinter``` window with a title "WiFi QR Code Generator".

```python
# Define the WiFi security types
security_types = ["WEP", "WPA/WPA2", "Open"]
```

This creates a list ```security_types``` that contains three options for the security types of the WiFi network.

```python
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
```

This defines the function ```generate_qr()``` that generates a QR code with the user's input for the network parameters. It first retrieves the input values for SSID, password, and security from the respective entry and dropdown widgets using the ```.get()``` method. Then it generates a QR code with the ```qrcode``` library using the ```add_data()``` method with the appropriate formatting for the WiFi network information. Finally, it saves the generated QR code as a PNG image.

```python
# Define the label and entry widgets for the SSID
ssid_label = tk.Label(root, text="SSID:")
ssid_label.pack()

ssid_entry = tk.Entry(root)
ssid_entry.pack()
```


This code defines the label and entry widgets for the SSID input field. It creates a ```tk.Label``` object with the text "SSID:" and adds it to the root window with the ```.pack()``` method. Then, it creates a ```tk.Entry``` object for the user to input the SSID and adds it to the root window with the ```.pack()``` method.

```python
# Define the label and entry widgets for the password
password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()
```


This code defines the label and entry widgets for the password input field. It creates a ```tk.Label``` object with the text "Password:" and adds it to the root window with the ```.pack()``` method. Then, it creates a ```tk.Entry``` object for the user to input the password and adds it to the root window with the ```.pack()``` method. The show option is set to '*' to display asterisks instead of plain text.

```python
# Define the label and dropdown widget for the security type
security_label = tk.Label(root, text="Security:")
security_label.pack()

security_var = tk.StringVar(root)
security_var.set(security_types[1])
security_dropdown = tk.OptionMenu(root, security_var, *security_types)
security_dropdown.pack()
```


This code defines the label and dropdown widgets for the security type input field. It creates a ```tk.Label``` object with the text "Security:" and adds it to the root window.

```python
# Define the label and dropdown widget for the security type
security_label = tk.Label(root, text="Security:")
security_label.pack()

security_var = tk.StringVar(root)
security_var.set(security_types[1])
security_dropdown = tk.OptionMenu(root, security_var, *security_types)
security_dropdown.pack()
```


This section of the code defines the label and dropdown widget for the security type input field. First, a ```tk.Label``` object is created with the text "Security:" and added to the root window using the ```.pack()``` method.

Next, a ```tk.StringVar``` object named ```security_var``` is created to store the selected security type from the dropdown. The initial value of ```security_var``` is set to ```security_types[1]```, which corresponds to ```"WPA/WPA2"```. This is done using the ```.set()``` method of ```security_var```.

Finally, a ```tk.OptionMenu``` object is created and added to the root window using the ```.pack()``` method. The ```OptionMenu``` object is assigned the ```security_var``` variable as its first argument, which indicates that it should display the value of ```security_var```. The second argument ```*security_types``` is a way of passing all the items in the ```security_types``` list as individual arguments to the ```OptionMenu``` constructor. This creates a dropdown menu with the options "WEP", "WPA/WPA2", and "Open".


```python
# Define the button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()
```

This section of the code defines the button to generate the QR code. A ```tk.Button``` object is created with the text "Generate QR Code" and the ```generate_qr``` function is assigned as its command. This means that when the button is clicked, the ```generate_qr``` function will be called. The button is added to the root window using the ```.pack()``` method.


```python
# Start the Tkinter event loop
root.mainloop()
```

This last line of code starts the ```Tkinter``` event loop, which listens for events such as button clicks and updates the GUI accordingly. The event loop continues running until the window is closed by the user.