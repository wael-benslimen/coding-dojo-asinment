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
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankaccount(0.2,100)
    
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"your balance is {self.account.balance}")
        return self
x = User("wael", "waelben1111@gmail.com")
x.make_deposit(50).display_user_balance().make_withdrawal(80).display_user_balance()