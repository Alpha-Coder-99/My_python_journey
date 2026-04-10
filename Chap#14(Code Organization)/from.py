# import ke saath aksar aapne from ka lafz bhi dekha hoga. 
# Ye dono mil kar kaam karte hain lekin inka tareeqa-e-kaara thora mukhtalif hai.
# Asan lafzon mein: "import poora dabba (module) utha kar laata hai, "
# "jabke from us dabbe ke andar se sirf aik khaas cheez (function ya variable) nikal kar laata hai."
# . from ... import * (The Dangerous Shortcut)
# Aapne kabhi kabhi ye bhi dekha hoga: from math import *
# Iska matlab hai: "Math ke andar jo kuch bhi hai, sab bahar nikal lo."
# Nuksan: Ye thora khatarnak hota hai kyunke agar aapke apne code mein bhi koi function usi naam ka hua, 
# toh confusion ho jayegi.
# Is liye professionals isay avoid karte hain.
# from math import pi 
# print(pi)

# from math import sqrt
# print(sqrt(4))

# from math import pow
# print(pow(2,3))
"We can import multiple function in any module "
"like this:"
from math import pow,sqrt,pi
print(sqrt(4))
print(pow(2,3))
print(pi)

