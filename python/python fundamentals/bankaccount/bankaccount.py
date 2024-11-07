class bankaccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
     self.balance = self.balance + amount
     return self
 
    def withdraw(self, amount):
        if self.balance > amount:
                self.balance = self.balance - amount
                return self
        else:
            print("insufitiont funds Charging a $5 fee")
            self.balance = self.balance - 5
            return self
 
    def display_accout_info(self):
        print(f"balace is : {self.balance}")
        return self
        
    def yeild_intrest(self):
        if self.balance > 0:
          self.balance = self.balance * self.int_rate
        return self

x = bankaccount(5, 100)
y = bankaccount(5, 150)
x.deposit(80).deposit(50).deposit(90).withdraw(50).yeild_intrest().display_accout_info()
y.deposit(50).deposit(90).withdraw(20).withdraw(10).withdraw(50).withdraw(90).yeild_intrest().display_accout_info()