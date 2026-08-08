class DataProcessor:
    # Ek hi method 'process', lekin ye alag alag inputs handle karega
    def process(self, data=None, scale_factor=None):
        
        # Case 1: Agar koi data nahi diya gaya
        if data is None:
            print("Error: Kuch toh data dein process karne ke liye!")
            
        # Case 2: Agar sirf data diya gaya aur scale_factor nahi (Text processing)
        elif scale_factor is None:
            print(f"Text Data Processing: {data.upper()}... (AI training ke liye tayyar hai)")
            
        # Case 3: Agar data aur scale dono diye gaye (Numerical processing)
        else:
            result = data * scale_factor
            print(f"Numerical Data Processing: {data} ko {scale_factor} se multiply kiya = {result}")

# --- Testing the Overloading ---

pro = DataProcessor()

# 1. Bina arguments ke (Empty Case)
pro.process()

# 2. Sirf ek argument ke sath (String Case)
pro.process("numpy")

# 3. Do arguments ke sath (Math Case)
pro.process(10, 5)