user_input = input("Enter your name: ")

if user_input.isalpha():
    print("Valid Name! Access Granted.")
else:
    print("Error: Name should only contain letters.")

#.isAlpha() ya btata ha aghr alphabets ha to a true
# Ye method check karta hai ke string mein sirf Letters (A-Z, a-z) hain ya nahi.

# Agar string mein sirf alphabets hain, to ye True return karta hai.

# Agar string mein Numbers, Spaces, ya Special Characters (@, #, $) hon, to ye False return deta hai.