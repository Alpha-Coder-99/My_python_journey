# 🟢 STEP #2 : LABEL kya hota hai?
# 💡 Simple meaning
# 👉 Label screen pe text show karta hai.
import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
label = tk.Label(root, text="Hello Areeba", font=("Arial", 20),fg="Red",bg="yellow")#root,text,font,color,background
label.pack()#scren pa show arna kalia
"""pack() widget ko visible banata hai
⚠️ Agar pack() na likho:
❌ label banega but show nahi hoga"""
root.mainloop()
"""👉 meaning:
Label() = text object banao
root = kis window ke andar show karna hai
text= = kya likhna hai"""
