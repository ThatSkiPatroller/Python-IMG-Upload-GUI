import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    # Open a file selection dialog
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    # Check if a file was selected
    if file_path:
        # Open selected image file
        image = Image.open(file_path)

        # Resize image if necessary
        # image = image.resize((width, height))

        # Display the image in the GUI
        image_label.config(image=image)
        image_label.image = image

# Create the main window
window = tk.Tk()
window.title("Program GUI")

# Create upload button
upload_button = tk.Button(window, text="Upload Image", command=open_image)
upload_button.pack()

# Create label to display image
image_label = tk.Label(window)
image_label.pack()

# button = tk.Button(window, text="Click me", command=button_click)
# button.pack()

window.mainloop()