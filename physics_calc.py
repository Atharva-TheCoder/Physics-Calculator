
while True:
    print("1. Velocity")
    print("2. Displacement")
    print("3. Time")
    print("4. Acceleration")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if (choice>=1 and choice<=4
):
       print ('Please enter the values in SI units only')

       if choice == 1:
          x = int(input("Displacement(x) : "))
          t = int(input("Time(t) : "))
          res = x/t
          print ("Result = ", res , "m/s")
       elif choice == 2:
          t = int(input("Time(t) : "))
          v = int(input("Velocity(v) : "))
          res = v*t
          print ("Result = ", res , "m")
       elif choice == 3:
          x = int(input("Displacement(x) : "))
          v = int(input("Velocity(v) : "))
          res = x/v
          print ("Result = ", res , "s")
       else:
          v = int(input("Velocity(v) : "))
          t = int(input("Time(t) : "))
          res = v/t
          print ("Result = ", res , "m/s²")
    elif choice == 5:
       exit()
    else:
       print ("Wrong input..!!")
