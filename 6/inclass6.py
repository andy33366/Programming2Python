from Bug import Bug
from Grasshopper import Grasshopper

def main():
    spider = Bug("Spider", 8, 0)
    hoppy = Grasshopper()

    spider.__str__()
    hoppy.__str__()
    hoppy.jump()
    hoppy.sound()


main()
