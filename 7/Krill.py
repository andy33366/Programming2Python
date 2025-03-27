#Krill

from Crustacean import Crustacean

class Krill(Crustacean):
    def __init__(self, name, legs, claws):
        super().__init__(name, legs, claws)
    def swim(self):
        print("*swim*")

