# 👉 tkinter Python ki built-in GUI library hai
# jo tumhe windows, buttons, labels, forms banane deti hai.
# 📚 Library hn ya module?
# ✔ technically: module + library dono type me count hoti hai
# ✔ Python ke andar already built-in aati hai (install nahi karni padti)
# 🧠 tkinter AI Engineer ke liye kya role hai?
# 👉 tkinter ka kaam:
# desktop apps banana 🖥️
# buttons, windows, forms
# simple GUI tools  
import tkinter as tk

# Window create
root = tk.Tk()
root.geometry("300x200")

# Function
def hello():
    print("Hello Areeba")

# Label
label = tk.Label(
    root,
    text="Hello Areeba",
    font=("Arial", 20),
    fg="red",
    bg="yellow"
)

label.pack(pady=20)#pady = widgets ke upar-neechay space dena ↕️

# Button
button = tk.Button(
    root,
    text="Click Me",
    font=("Arial", 15),
    fg="white",
    bg="blue",
    command=hello
)

button.pack()

# Run window
root.mainloop()