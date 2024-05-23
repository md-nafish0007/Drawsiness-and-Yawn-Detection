import tkinter as tk
from tkinter import filedialog, messagebox
import os

def open_file():
    file_path = "drowsiness_yawn.py"
    if os.path.isfile(file_path):
        os.system(f'python "{file_path}"')
    else:
        messagebox.showerror("File Not Found", f"Cannot find {file_path}")

def create_gradient(canvas, color1, color2):
    """Create a gradient background on the canvas"""
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    for i in range(height):
        r = int(r1 + (r2 - r1) * i / height)
        g = int(g1 + (g2 - g1) * i / height)
        b = int(b1 + (b2 - b1) * i / height)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)

 #def center_frame(frame, root):
  #  """Center the frame within the root window."""
   # root.update_idletasks()  # Ensure the window dimensions are updated
    #window_width = root.winfo_width()
    #window_height = root.winfo_height()
    #frame_width = frame.winfo_reqwidth()
    #frame_height = frame.winfo_reqheight()
    #center_x = (window_width - frame_width) // 2
    #center_y = (window_height - frame_height) // 2
    #frame.place(x=center_x, y=center_y) 

def center_frame(frame, root):
    """Center the frame in the window."""
    frame.place(relx=0.5, rely=0.5, anchor='center')

root = tk.Tk()
frame = tk.Frame(root)
transparent_frame = tk.Frame(root, bg="white")

root.bind('<Configure>', lambda event: center_frame(transparent_frame, root))

def on_resize(event):
    """Handle window resize event to keep the frame centered."""
    create_gradient(canvas, (0, 0, 128), (128, 128, 255))  # Recreate gradient on resize
    center_frame(transparent_frame, root)


frame = tk.Frame(root)
root.bind('<Configure>', on_resize)  # Bind the resize event to the on_resize function
root.title("Drowsiness and Yawn Detector System")
#root.geometry("800x600")  # Set the window size


canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)


canvas.update()  # Ensure canvas dimensions are updated before drawing the gradient
create_gradient(canvas, (0, 0, 128), (128, 128, 255))


transparent_frame = tk.Frame(root, bg="white")
transparent_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Temporary center placement
transparent_frame = tk.Frame(root, width=400, height=800, bg="white")


title_label = tk.Label(transparent_frame, text="Drowsiness and Yawn Detection System with Voice Alerts", font=("Arial", 24, "bold"), bg="white", fg="navy")
title_label.pack(pady=10)


subtitle_label = tk.Label(transparent_frame, text="Made by MD Nafish", font=("Arial", 14), bg="white", fg="navy")
subtitle_label.pack(pady=5)


open_button = tk.Button(transparent_frame, text="Open App", command=open_file, font=("Arial", 14), bg="lightblue", fg="white", padx=20, pady=10)
open_button.pack(pady=20)


root.resizable(True, True)
root.after(100, lambda: center_frame(transparent_frame, root))
root.update()  # Ensure the window is updated and responsive

root.mainloop()
