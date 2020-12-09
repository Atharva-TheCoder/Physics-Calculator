
#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (red+"""

(  _ \( )_( )( \/ )/ __)(_  _)/ __)/ __)  / __)  /__\  (  )  / __)
 )___/ ) _ (  \  / \__ \ _)(_( (__ \__ \ ( (__  /(__)\  )(__( (__ 
(__)  (_) (_) (__) (___/(____)\___)(___/  \___)(__)(__)(____)\___)
                                                         v 1.0
"""+red) 
print (lgreen+bold+"    <===[[ coded by @tharva-TheHacker ]]===> \n"+clear)

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
