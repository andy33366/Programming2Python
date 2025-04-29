from PIL import Image, ImageTk

class Animal:
    def __init__(self, name, habitat, description, image_path):
        self.name = name
        self.habitat = habitat
        self.description = description
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)

    def get_name(self):
        return self.name

    def get_habitat(self):
        return self.habitat

    def get_desc(self):
        return self.description

    def get_img(self):
        return self.tk_image


