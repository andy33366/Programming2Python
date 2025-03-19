from Bug import Bug

class Grasshopper(Bug):
    def __init__(self, name = "Grasshopper", legs = 6, wings = 4):
        super().__init__(name, legs, wings)

    def jump(self):
         print("hop, hop")

    def sound(self):
        print("*cricket* *cricket*")

