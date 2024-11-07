class pet:
    def __init__(self, name, type, tricks, health, energie):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energie = energie
    def sleep(self):
        self.energie = self.energie + 25
        print("pet rested")
        return self
    def eat(self):
        self.energie = self.energie + 5
        self.health = self.health + 10
        print("pet ate")
        return self
    def play(self):
        self.health = self.health + 5
        print("pet having fun")
        return self
    def sound(self):
        print("pet sound")
        return self
        