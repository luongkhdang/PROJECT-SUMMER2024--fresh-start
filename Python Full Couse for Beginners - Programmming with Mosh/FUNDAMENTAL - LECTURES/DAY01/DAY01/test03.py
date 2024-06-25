"""

Game:
start - to start the car
stop - stop
quit - to exit



return

"""

command = ""
car_started = False

while True:
    command = input("> ").lower()

    if command == "start" :
        if car_started:
            print("Car is already started ...")
        else:
            print("Car started ...")
            car_started = True
    elif command== "stop" :
        if not car_started:
            print("Car is already stopped ...")
        else:
            print("Car stopped.")
            car_started = False
    elif command == "help":
        print("""Game:
start - to start the car
stop - stop
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")

