#!/bin/python

#Copyright  TigerClips1 © 2023 all rights reserved

import os #import os mudules

name = input("Please Enter your  linux name on your linux PC or WSL or VM: ") #ask for the Linux username

print("if you don't know the path to your USb run the runmefirst.sh then you will see your usb path\n")

USB = input("Please Enter your USB dircotry name: ") #ask the user for the usb name which can be obtained on the RunMefirst.sh

Arch = "sudo pacman -Syyu && sudo pacman -S wget" #install Requirement for Arch base distro

Fedora = "sudo dnf update && sudo dnf install wget" #install Requirement for Fedora base distro

credit = "Script By TigerClips1" #give me credit

kofi = "https://ko-fi.com/tigerclips1" #support me on my kofi

promo = "ps4linux.com" #promote PS4linux.com

error2 = "You don't have an arch base distro" #print error on the screen

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

change = f"/media/{name}/{USB}" #change directories

make = f"sudo mkdir PS4" #make directory

change2 = f"/media/{name}/{USB}/PS4/" #change directory

make2 = "sudo mkdir UPDATE" #make directory

change3 = f"/media/{name}/{USB}/PS4/UPDATE" #change directories

def menu (): #function to keep things nice
    while True: #loop the menu
    
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

        option = input("Enter the PS4 firmware you want to install: ") #get input from user


        
        if option == "1":   #if option1 is selected then it will install PS4 9.00 Normal Firmware Update
            
            os.system(PS4_900) #this download the 9.00 Normal Firmware Update to your USB

    
        elif option == "2": #if option2 is selected then it will install PS4 5.05 Normal Firmware Update
        
            os.system(PS4_505)  #this download the 5.05 Normal Firmware Update to your USB
    
        elif option == "3": #if option3 is selected then it will install PS4 7.55 Normal Firmware Update
        
            os.system(PS4_755)  #this download the 7.55 Normal Firmware Update to your USB
         
        elif option == "4": #if option4 is selected then it will install PS4 7.02 Normal Firmware Update
        
            os.system(PS4_702)  #this download the 7.02 Normal Firmware Update to your USB
    
        elif option == "5": #if option5 is selected then it will install PS4 6.72 Normal Firmware Update
        
            os.system(PS4_672)  #this download the 6.72 Normal Firmware Update to your USB
    
        elif option == "6": #if option6 is selected then it will install PS4 4.55 Normal Firmware Update
     
            os.system(PS4_455)  #this download the 4.55 Normal Firmware Update to your USB
        
        elif option == "7": #if option7 is selected then it will install PS4 4.05 Normal Firmware Update
        
            os.system(PS4_405)  #this download the 4.05 Normal Firmware Update to your USB

        elif option == "8": #if option8 is selected then it will install PS4 1.76 Normal Firmware Update
        
            os.system(PS4_176)  #this download the 1.76 Normal Firmware Update to your USB

        elif option == "9": #if option1 is selected then it will load the 2 menu
        
            menu2() #call menu2 function
    
        elif option == "10": #if the player hit exit then this will call this if statement
            break#break out of the loop when you type 10
            
        
            print(credit, sep= "\n") #print the credit on the screen when done
        
            print(kofi, sep = "\n") #print my kofi page on the screen
        
            print(promo, sep = "\n") #promote ps4linux.com
        
            exit() #exit the program
        
        else:
          print("Invalid option. Please try again.") #print the error on your screen
          

def menu2(): #function to keep thing nice
    while True: #loop the menu

        print ("[1]You want To Install Recovery  9.00 PS4 Update to your USB") #print text of the menu on the screen
    
        print ("[2]You want To Install Recovery 5.05 PS4 Update to your USB") #print text of the menu on the screen
    
        print ("[3]You want To Install Recovery 7.55 PS4 Update to your USB") #print text of the menu on the screen
    
        print ("[4]You want To Install Recovery 7.02 PS4 Update to your USB") #print text of the menu on the screen
    
        print ("[5]You want To Install Recovery 6.72 PS4 Update to your USB") #print text of the menu on the screen
    
        print ("[6]You want To Install Recovery 4.55 PS4 Update to your USB") #print text of the menu on the screen
    
        print ("[7]You want To Install Recovery 4.05 PS4 Update to your USB") #print text of the menu on the screen
    
        print ("[8]You want To Install Recovery 1.76 PS4 Update to your USB") #print text of the menu on the screen
    
        print("[9]Back") #print text of the menu on the screen
        
        option = input("Enter the PS4 firmware you want to install: ") #get input from user

        
        if option == "1": #if statement
    
            os.system(PS4_Recovery_900) #if you type one then it will install PS4 9.00 Recovery
    
        elif option == "2": #elif statement
    
            os.system(PS4_Recovery_505) #if you type one then it will install PS4 5.05 Recovery
        elif option == "3": #elif statement
    
            os.system(PS4_Recovery_755) #if you type one then it will install PS4 7.55 Recovery

        elif option == "4": #elif statement
    
            os.system(PS4_Recovery_702) #if you type one then it will install PS4 7.02 Recovery

        elif option == "5": #elif statement
    
            os.system(PS4_Recovery_672) #if you type one then it will install PS4 6.72 Recovery

        elif option == "6": #elif statement
    
            os.system(PS4_Recovery_455) #if you type one then it will install PS4 4.55 Recovery

        elif option == "7": #elif statement
    
            os.system(PS4_Recovery_405) #if you type one then it will install PS4 4.05 Recovery

        elif option == "8": #elif statement
    
            os.system(PS4_Recovery_176) #if you type one then it will install PS4 1.76 Recovery

        elif option == "9": #elif statement
            break #break out of the loop once you type 9
        else:
            print("Invalid option. Please try again.") #print the error on your screen

def linux2(): #function keep things nice
    
    ArchLinux = os.popen(Arch) # this function will install all requirement on arch base distro
    
    output2 = ArchLinux.readlines() #check if you on a arch base distro
    
    print(error2) #print error on your screen

def linux3(): #function keep things nice
    
    FedoraLinux = os.popen(Fedora) #this function will install all requirements on fedora base distro
    
    output3 = FedoraLinux.readlines() #check if you on a fedora based distro
    
    print(error3)#print error on your screen

def credits(): #function
    
    print(credit, sep= "\n") #print the credit on the screen when done
        
    print(kofi, sep = "\n") #print my kofi page on the screen
        
    print(promo, sep = "\n") #promote ps4linux.com

def Main(): #function
        os.chdir(change)#change directories
    
        os.system(make)#make directories
    
        os.chdir(change2) #change directories
    
        os.system(make2) #make directories
    
        os.chdir(change3) #change directories

linux2()#call the function

linux3() #call the function

Main() #call the function

menu() #call the function

credits() #call the function


## kill me lol jk ##