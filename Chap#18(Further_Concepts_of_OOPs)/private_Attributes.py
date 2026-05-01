#private attributes and methods are meant to be used only within the class and are not accessible from outside the class
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self._acc_pass=acc_pass
    def reset_pass(self):
        print(self._acc_pass)

acc1=Account("12345","abcd")

print(acc1._acc_pass)
print(acc1.reset_pass())
