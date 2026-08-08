# Parent Class (Baap)
class AIModel:
    def predict(self):
        print("Mera kaam sirf prediction karna hai, lekin mujhe nahi pata kaise.")

# Child Class 1 (Beta 1)
class LinearRegression(AIModel):
    # Method Overriding: Baap ke 'predict' ko apni marzi se badal diya
    def predict(self):
        print("Main Maths ke formula se prediction kar raha hoon.")

# Child Class 2 (Beta 2)
class NeuralNetwork(AIModel):
    # Method Overriding: Baap ke 'predict' ko dobara badal diya
    def predict(self):
        print("Main Brain-like neurons use kar ke prediction kar raha hoon.")

# --- Testing ---
models = [LinearRegression(), NeuralNetwork()]

for model in models:
    model.predict()