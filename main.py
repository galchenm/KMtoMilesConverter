from tkinter import Tk, Label, Entry, Button

# Create the main window
window = Tk()

# Set the title of the window
window.title("KM to Miles Converter")

# Create a label to prompt the user
label = Label(window, text="Enter distance in km:")
label.pack()

# Create a text box for user input
km_entry = Entry(window)
km_entry.pack()

# Function to greet the user based on input
def convert():
  km = km_entry.get()  # Get the text from the entry box
  miles = float(km) / 1.609
  output_message = f"Distance in miles: {miles:.2f}!"
  output_label = Label(window, text=output_message)
  output_label.pack()


button = Button(window, text="Convert", command=convert)
button.pack()

# Start the main event loop
window.mainloop() 
