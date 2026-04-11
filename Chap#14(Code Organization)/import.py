# import Python ka wo khas hukam (command) hai jo doosri files ya toolboxes se code ko aapki mojooda file mein lekar aata hai.
# Asan lafzon mein: "Import ka matlab hai kisi baahar ki cheez ko apne andar shamil karna."
# AI Rule = AI projects import ke baghair shuru hi nahi hote.
import math


print(math.sqrt(6))
print(math.factorial(3))

import numpy as np # Hum 'as np' isliye likhte hain taakay short ho jaye

# Ek simple NumPy Array banate hain
my_array = np.array([1, 2, 3, 4, 5])

print("Mera Pehla AI Array:", my_array)
print("Array ki Type:", type(my_array))