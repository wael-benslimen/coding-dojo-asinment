from ninja_class import *
from pet_class import *

p = pet("lucky", "dog", "sit", 100, 100)
nin = ninja("wael", "benslimen", p , "kible", "dryfood")

nin.feed().walk().bathe()
