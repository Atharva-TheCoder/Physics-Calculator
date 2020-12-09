
#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (yellow+"""
 ____  _  _  _  _  ____  __  ___  ____    ___   __   __     ___ 
(  _ \/ )( \( \/ )/ ___)(  )/ __)/ ___)  / __) / _\ (  )   / __)
 ) __/) __ ( )  / \___ \ )(( (__ \___ \ ( (__ /    \/ (_/\( (__ 
(__)  \_)(_/(__/  (____/(__)\___)(____/  \___)\_/\_/\____/ \___) """+yellow) 
print (lgreen+"""                                                        (v 1.0)"""+lgreen)
                                                         
print (lgreen+bold+"          <===[[ coded by @tharva-TheHacker ]]===> \n"+clear)

while True:
    print(cyan+"1. Velocity"+cyan)
    print(cyan+"2. Displacement"+cyan)
    print(cyan+"3. Time"+cyan)
    print(cyan+"4. Acceleration"+cyan)
    print(cyan+"5. Exit"+cyan)
    choice = int(input("Enter your choice: "))
    if (choice>=1 and choice<=4
):
       print ('Please enter the values in SI units only')

       if choice == 1:
          x = int(input("Displacement(x) : "))
          t = int(input("Time(t) : "))
          res = x/t
          print ("[Result] = ", res , "m/s")
       elif choice == 2:
          t = int(input("Time(t) : "))
          v = int(input("Velocity(v) : "))
          res = v*t
          print ("[Result] = ", res , "m")
       elif choice == 3:
          x = int(input("Displacement(x) : "))
          v = int(input("Velocity(v) : "))
          res = x/v
          print ("[Result] = ", res , "s")
       else:
          v = int(input("Velocity(v) : "))
          t = int(input("Time(t) : "))
          res = v/t
          print ("[Result] = ", res , "m/s²")
    elif choice == 5:
       exit()
    else:
       print (red+"Wrong input..!!"+red)
