from Exhibit import Exhibit
from Everglades import Everglades

def main():
    #creates a tundra exhibit
    tundra = Exhibit("Arctic Tundra", 12, 75)
    #creates an everglades object
    glades = Everglades(5)
    tundra.__str__()
    glades.__str__()
main()
