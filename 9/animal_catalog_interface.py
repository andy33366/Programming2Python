import tkinter as tk
from PIL import ImageTk, Image
from Animal import Animal

root = tk.Tk()

root.title("Museum Catalog")
root.geometry("700x500")
#catalog class which includes animal objects
class Catalog():
    def __init__(self, animal1, animal2, animal3):
        self.animals = [animal1, animal2, animal3]
        self.choices = [self.animals[0].get_name(), self.animals[1].get_name(), self.animals[2].get_name()]

#hardocded set of animals for the catalog
cat = Animal("Cat", "House", "A cute 4 legged creature", "cat.webp")
grasshopper = Animal("Grasshopper", "Everglades", "Hopps Grass", "grasshopper.png")
mouse = Animal("Mouse", "House", "is eaten by cats", "mouse.jpg")

menu = Catalog(cat, grasshopper, mouse)
menuOption = tk.StringVar(value=menu.choices[0])

#called whenever the user changes option
def optionChanged(*args):
    selected = menuOption.get()
    #if animal is the one user selects
    for animal in menu.animals:
        if animal.get_name() == selected:
            #update gui to show selected animal
            name_label.config(text=animal.get_name())
            habitat_label.config(text=animal.get_habitat())
            desc_label.config(text=animal.get_desc())
            image_label.config(image=animal.get_img())
            image_label.image = animal.get_img()
            break

#tracks change and sends it to optionChanged
menuOption.trace("w", optionChanged)

option_menu = tk.OptionMenu(root, menuOption, *menu.choices)
option_menu.pack()
    
#creates a default otherwise nothing shows up
default = menu.animals[0]
name_label = tk.Label(root, text=default.get_name())
name_label.pack()
habitat_label = tk.Label(root, text=default.get_habitat())
habitat_label.pack(pady=10)
desc_label = tk.Label(root, text=default.get_desc())
desc_label.pack()
img = default.get_img()
image_label = tk.Label(root, image=img)
image_label.image = img
image_label.pack(padx=10, pady=10)


root.mainloop()
