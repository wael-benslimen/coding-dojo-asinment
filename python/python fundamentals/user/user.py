class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f"first name is{self.first_name}")
        print(f"last name is {self.last_name}")
        print(f"emai : {self.email}")
        print(f"age : {self.age}")
        print(f"reward mumber status : {self.is_rewards_member}")
        print(f"gold cad points = {self.gold_card_points}")
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

x = user("wael", "benslimen", "waelbeslimen111@gmail.com", "21")
y = user("jane", "doe", "janedoe@gmail.com", "21")
z = user("eren", "yeagar", "eren111@gmail.com", "25")
x.enroll()
x.spend_points(50)
y.enroll()
y.spend_points(80)
x.display_info()
y.display_info()
z.display_info()
