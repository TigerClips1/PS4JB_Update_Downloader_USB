#!/bin/python

#Copyright  TigerClips1 © 2023 all rights reserved

import os #import os mudules

name = input("Please Enter your  linux name on your linux PC or WSL or VM: ") #ask for the Linux username

USB = input("Please Enter your USB dircotry name: ") #ask the user for the usb name witch can be obtain on the RunMefirst.sh


Arch = "sudo pacman -Syyu && sudo pacman -S wget" #install Requirement for Arch base distro

Fedora = "sudo dnf update && sudo dnf install wget" #install Requirement for Fedora base distro

credit = "Script By TigerClips1" #give me credit

kofi = "https://ko-fi.com/tigerclips1" #support me on my kofi

promo = "ps4linux.com" #promote PS4linux.com


error2 = "Yu don't have an arch base dsitro" #print error on the screen

error3 = "You don't have an fedora base distro" #print error on the screen

PS4_900 = "wget https://archive.org/download/PS4-System-Firmwares/Firmware%209.00/PS4UPDATE.PUP"#download the 9.00 normal firmware

PS4_505 = "wget https://archive.org/download/PS4-System-Firmwares/Firmware%205.05/PS4UPDATE.PUP"#download the 5.05 normal firmware

PS4_755 = "wget https://archive.org/download/PS4-System-Firmwares/Firmware%207.55/PS4UPDATE.PUP" #download the 7.55 normal firmware

PS4_702 = "wget https://archive.org/download/PS4-System-Firmwares/Firmware%207.02/PS4UPDATE.PUP" #download the 7.02 normal firmware

PS4_672 = "wget https://archive.org/download/PS4-System-Firmwares/Firmware%206.72/PS4UPDATE.PUP" #download the 6.72 normal firmware

PS4_455 = "wget https://archive.org/download/PS4-System-Firmwares/Firmware%204.55/PS4UPDATE.PUP" #download the 4.55 normal firmware

PS4_405 = "wget https://archive.org/download/PS4-System-Firmwares/Firmware%204.05/PS4UPDATE.PUP" #download the 4.05 normal firmware

PS4_176 = "wget https://archive.org/download/PS4-System-Firmwares/Firmware%201.76/PS4UPDATE.PUP" # download the 1.76 normal firmware

PS4_Recovery_900 = "wget https://archive.org/download/PS4-Recovery-Firmwares/Firmware%209.00/PS4UPDATE.PUP" #download the PS4 9.00 Recovery firmware

PS4_Recovery_505 = "wget https://archive.org/download/PS4-Recovery-Firmwares/Firmware%205.05/PS4UPDATE.PUP"  #download the PS4 5.05 Recovery firmware

PS4_Recovery_755 = "wget https://archive.org/download/PS4-Recovery-Firmwares/Firmware%207.55/PS4UPDATE.PUP" #download the  PS4 7.55 Recovery firmware

PS4_Recovery_702 = "wget https://archive.org/download/PS4-Recovery-Firmwares/Firmware%207.02/PS4UPDATE.PUP"  #download the PS4 7.02 Recovery firmware

PS4_Recovery_672 = "wget https://archive.org/download/PS4-Recovery-Firmwares/Firmware%206.72/PS4UPDATE.PUP"  #download the PS4 6.72 Recovery firmware

PS4_Recovery_455 = "wget https://archive.org/download/PS4-Recovery-Firmwares/Firmware%204.55/PS4UPDATE.PUP"  #download the PS4 4.55 Recovery firmware

PS4_Recovery_405 = "wget https://archive.org/download/PS4-Recovery-Firmwares/Firmware%204.05/PS4UPDATE.PUP"  #download the PS4 4.05 Recovery firmware

PS4_Recovery_176 = "wget https://archive.org/download/PS4-Recovery-Firmwares/Firmware%201.76/PS4UPDATE.PUP"  #download the PS4 1.76 Recovery firmware

change = f"/media/{name}/{USB}" #change directorys

make = f"sudo mkdir PS4" #make directory

change2 = f"/media/{name}/{USB}/PS4/" #change directory

make2 = "sudo mkdir UPDATE" #make directory

change3 = f"/media/{name}/{USB}/PS4/UPDATE" #change directorys

def menu (): #function to keep thing nice
    
    print ("[1]You want To Install 9.00 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[2]You want To Install 5.05 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[3]You want To Install 7.55 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[4]You want To Install 7.02 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[5]You want To Install 6.72 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[6]You want To Install 4.55 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[7]You want To Install 4.05 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[8]You want To Install 1.76 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[9]Next Page") #print text of the menu on the screen

    print ("[10]EXIT") #print text of the menu on the screen

menu()#call the function

option = int(input('Enter your PS4 firmware: ')) #get input from user when using the menu

def menu2(): #function to keep thing nice
    print ("[11]You want To Install Recovery  9.00 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[12]You want To Install Recovery 5.05 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[13]You want To Install Recovery 7.55 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[14]You want To Install Recovery 7.02 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[15]You want To Install Recovery 6.72 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[16]You want To Install Recovery 4.55 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[17]You want To Install Recovery 4.05 PS4 Update to your USB") #print text of the menu on the screen
    
    print ("[18]You want To Install Recovery 1.76 PS4 Update to your USB") #print text of the menu on the screen
    
    print("[19]Back") #print text of the menu on the screen
    
    print ("[20]EXIT") #print text of the menu on the screen 



def linux2(): #function keep thing nice
    
    ArchLinux = os.popen(Arch) # this function will install all requriement on arch base distro
    
    output2 = ArchLinux.readlines() #check if you on a arch base distro
    
    print(error2) #print error on your screen
#TODO comeplate the readme with Kwhitehead07  and add comments to all the other code fix spelling error tomorrow

def linux3():
    
    FedoraLinux = os.popen(Fedora)
    
    output3 = FedoraLinux.readlines()
    
    print(error3)

def Main():
    os.chdir(change)
    
    os.system(make)
    
    os.chdir(change2)
    
    os.system(make2)
    
    os.chdir(change3)
    
    if option == 1:
        os.system(PS4_900)
    
    else:
        
        print("you did not want to install PS4 9.00")
    
    if option == 2:
        
        os.system(PS4_505)
    else:
        
        print("you do not want to install Ps4 5.05")
   
    if option == 3:
        
        os.system(PS4_755)
    
    else:
        
        print("You do not want to install 7.55 PS4")
    
    if option == 4:
        
        os.system(PS4_702)
    
    else:
        
        print("you do not want to install PS4 7.02 ")
    
    if option == 5:
        
        os.system(PS4_672)
    
    else:
        
        print("you do not want to install PS4 6.72")
    
    if option == 6:
     
     os.system(PS4_455)
    
    else:
        
        print("you don't want to install PS4 4.55")
    
    if option == 7:
        
        os.system(PS4_405)
    
    else:
        
        print("you dont't want to install PS4 4.05")
    
    if option == 8:
        
        os.system(PS4_176)
    
    else:
        
        print("You  dont want to install PS4 1.76")
    
    if option == 9:
        
        menu2()
        
        option2 = int(input('Enter your PS4 firmware: '))
    
    if option2 ==  19:
        
            menu()
        
        
            option2 = int(input('Enter your PS4 firmware: '))

    if option == 10:
        
        print(credit, sep= "\n")
        
        print(kofi, sep = "\n")
        
        print(promo, sep = "\n")
        
        exit()

    if option2 == 1:
        os.system(PS4_900)
    else:   
            print("you did not want to install PS4 9.00")
    
    if option2 == 2:
        
        os.system(PS4_505)
    else:
        
        print("you do not want to install Ps4 5.05")
   
    if option2 == 3:
        
        os.system(PS4_755)
    
    else:
        
        print("You do not want to install 7.55 PS4")
    
    if option2 == 4:
        
        os.system(PS4_702)
    
    else:
        
        print("you do not want to install PS4 7.02 ")
    
    if option2 == 5:
        
        os.system(PS4_672)
    
    else:
        
        print("you do not want to install PS4 6.72")
    
    if option == 6:
     
     os.system(PS4_455)
    
    else:
        
        print("you don't want to install PS4 4.55")
    
    if option2 == 7:
        
        os.system(PS4_405)
    
    else:
        
        print("you dont't want to install PS4 4.05")
    
        if option2 == 8:
        
            os.system(PS4_176) 
        else:
            print("You  dont want to install PS4 1.76")
    if option2 == 9:
        menu2()
    
    option2 = int(input('Enter your PS4 firmware: '))

    if option2 == 20:

            
        print(credit, sep= "\n")
        
        print(kofi, sep = "\n")
        
        print(promo, sep = "\n")
        
        exit()

def Main2():   
    if option2 == 11:
    
        os.system(PS4_Recovery_900)

    else:
    
        print("You don't want to install PS4 9.00 Recovery")

    if option2 == 12:
    
        os.system(PS4_Recovery_505)

    else:
    
        print("you don't want to install PS4 5.05 Recovery")

    if option2 == 13:
    
        os.system(PS4_Recovery_755)

    else:
    
        print("you don't want to install PS4 7.55 Recovery")

    if option2 == 14:
    
        os.system(PS4_Recovery_702)

    else:
    
        print("you don't want to install PS4 7.02 Recovery")

    if option2 == 15:
    
        os.system(PS4_Recovery_672)
    else:
    
        print("you don't want to install PS4 6.72 Recovery")

    if option2 == 16:
    
        os.system(PS4_Recovery_455)

    else:
    
        prnt("you don't want to install PS4 4.55 Recovery")

    if option2 == 17:
    
        os.system(PS4_Recovery_405)

    else:
    
        print("you don't want to install PS4 4.05 Recovery")

    if option2 == 18:
    
        os.system(PS4_Recovery_176)

    else:
    
        print("you don't want to install PS4 1.76 Recovery")

linux1() #call the function

linux2()#call the function

linux3() #call the function

Main() #call the function

Main2() #call the function
