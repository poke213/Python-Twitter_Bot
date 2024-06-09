import tkinter as tk
from tkinter import messagebox

def show_popup():
    # This function will be called to show the popup window
    messagebox.showinfo("Popup", "Time's up!")
    start_timer(timer_duration)  # Restart the timer after showing the popup

def start_timer(seconds):
    # This function will start the timer and call the show_popup function after the specified time
    root.after(seconds * 1000, show_popup)  # Multiply by 1000 to convert seconds to milliseconds

# Create the main window
root = tk.Tk()
root.title("Timer Popup")

# Set the timer duration (in seconds)
timer_duration = 20  # Change this value to set a different timer duration

# Create a label to inform the user about the timer
label = tk.Label(root, text=f"A popup will appear every {timer_duration} seconds.")
label.pack(pady=20)

# Start the timer
start_timer(timer_duration)

# Run the main event loop
root.mainloop()