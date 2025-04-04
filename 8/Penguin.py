from Bird import Bird

class Penguin(Bird):
    def __init__(self, name = "Penguin"):
        super().__init__(name)

    def __str__(self):
        print(f"This is a {self.name}. {self.name}s use countershading as camoflauge.")

    def fly(self):
        print(f"the {self.name} cannot fly")

    def eat(self):
        print(f"the {self.name} eats krill, squid, and small fishes")

    def swim(self):
        print(f"the {self.name} can swim around 4 to 7 mph")


