import datetime
# so i dont have to write time twice
from Time import Time as Time 


def main():
    
    now = datetime.datetime.now()

    time0 = Time(now.hour, now.minute, now.second)


    print("current time is: ", str(now.hour), str(now.minute))


main()


