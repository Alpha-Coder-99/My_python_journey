"""🟢 STEP #4 — Entry (Input box)
💡 Entry kya hota hai?
👉 Entry = user se text input lene ka box
Jaise:
name likhna
number enter karna
message type karna"""
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack()

root.mainloop()