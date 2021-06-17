quit = 0
turn_on = False
print("Start - To start the car")
print("Stop - To stop the car")
print("Quit - To quit the game")

while quit == 0:
   command = input("> ").title()
   if command == "Start":
       if turn_on == True:
           print("The car was already started.")
       else:
           print("The car is now started, ready to go.")
           turn_on = True
   elif command == "Stop":
       if turn_on == False:
           print("The car was already stopped.")
       else:
           print("The car is stopped.")
           turn_on = False
   elif command == "Quit":
       quit = 1
   else:
       print("Wrong command.")
print("See you next time.")