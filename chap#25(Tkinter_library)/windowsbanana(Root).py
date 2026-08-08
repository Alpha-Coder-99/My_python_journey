# 🟢Windows banana (Root)
#Koe bhi app banana kalai hum k khali windo wki zarorrat hoi hn
# 1.tkinetr ko imprt karna
import tkinter as tk 
"uper hum na tkinetr libaray ko import kia aur phir us ka nickname tk introduce karya"
#2.khal window banana
root=tk.Tk()
"""👉 yeh sab se important line hai:
Tk() = new window create karta hai
root = us window ka naam (variable)
📌 simple meaning:
“ek blank app window bana do”"""
# 🏷️ 3. Title set karna
root.title("My app")
# 📏 4. Size set karna
root.geometry("300x200")
"""👉 window ka size define karta hai:

300 = width
200 = height

📌 matlab:

“window kitni bari hogi screen pe”"""
# 🔁 5. Window ko chalana
root.mainloop()
"""👉 yeh sab se zaroori line hai

📌 simple meaning:

“window ko open rakhna aur live chalana”

Agar yeh na ho:
❌ window 1 second me band ho jati hai"""

#Full idea 
"""👉 Tkinter me tum yeh karti ho:
library import 📦
window banati ho 🪟
uska name set karti ho 🏷️
size set karti ho 📏
aur run karti ho 🔁
 """
"""| Code     | Meaning             |
| -------- | ------------------- |
| Tk()     | blank room 🏠       |
| title    | room ka naam        |
| geometry | room ka size        |
| mainloop | room ko open rakhna |
"""


