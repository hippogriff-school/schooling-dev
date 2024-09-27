#Based off original code "flowcharts" in the ClassWork folder.
#This is a copy where there is the option for a second cup using left over water.

import time

def firsttea():

    time.sleep(1)
    print("Get a Mug.")
    time.sleep(1)
    print("Add a tea bag")
    time.sleep(1)           
    print("Boil Water")
    time.sleep(1)
    print("Pour water into cup")
    time.sleep(1)
    print("Remove tea bag from mug")

    decision2 = input("Do you want milk? y/n: ")

    if decision2 == ("y"):
        print("Ok, milk added.")
        
    if decision2 == ("n"):
        print("Ok, NO milk added.")

    time.sleep(1)
    decision3 = input("Do you want sugar? y/n: ")

    if decision3 == ("y"):
         print("Ok, sugar added.")
        
    if decision3 == ("n"):
         print("Ok, NO sugar added.")

    time.sleep(1)
    print("Drink your tea!")

def teatwo():

    time.sleep(1)
    print("Get a Mug.")
    time.sleep(1)
    print("Add a tea bag")
    time.sleep(1)           
    print("Use other water")
    time.sleep(1)
    print("Pour water into cup")
    time.sleep(1)
    print("Remove tea bag from mug")

    decision2 = input("Do you want milk? y/n: ")

    if decision2 == ("y"):
        print("Ok, milk added.")
        
    if decision2 == ("n"):
        print("Ok, NO milk added.")

    time.sleep(1)
    decision3 = input("Do you want sugar? y/n: ")

    if decision3 == ("y"):
         print("Ok, sugar added.")
        
    if decision3 == ("n"):
         print("Ok, NO sugar added.")

    time.sleep(1)
    print("Drink your tea!")
        

print("Hello World!")

while True:

    decision = input("Do you want tea? y/n: ")

    if decision == ("y"):
        print("Ok, lets get started.")
        print(firsttea())
    
    if decision == ("n"):
        print ("Well why did you open this then.")
        break

    while True:

        moretea = input("Do you want another cup? y/n: ")

        if moretea == ("y"):
            print("Ok, this will be a bit differant")
            print(teatwo())
            
        if moretea== ("n"):
            print("Bye then!")
            break
