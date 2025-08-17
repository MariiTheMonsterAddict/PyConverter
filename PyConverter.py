import sys
import os
import time
import json 
from pathlib import Path
#TODO Import save file functionality so the settings menu actually does something...
#TODO Finish the personal config setting 
#TODO make it so the program only displays the info you ask for in the config
#TODO default to showing all the values and asking for what keys to use only if there is no personalconfig
#TODO make it ask for the file name if there is no default set 
#TODO make it so it asks the user for what they want stripped out of the input
#TODO finish the program!
#TODO make it output to a txt file with some pretty formating for easy reading 
#TODO make a readme with some basic instructions
#TODO post to a repo on github!!


outputfilename = "output.txt"
#you can make it faster by making this variable 0, I like it at 1, but its not me using it
timevariable = 0
#change this to wherever your gonna download the output files
#for ease of use just change the output file to the same name every time and slap it here, mainly for automation purposes
#script will ask you for a location if this is 
path = "/home/mari/Downloads"
os_sys = sys.platform
#you can put parts of the known keyvalues in this config file and it'll fast track the sorting operations
personalconfig="score,hp,playerId"
data_dict = {}

#Dont go beyond this line if you don't understand what an int is in python... pls you'll probably break it and post a bug report on github... ;c
#-----------------------------------------------------------------------------------------------------------------------------------------------------

def main():


    def startup_sequence():
        print("Preparing script!")
        script_path = os.path.realpath(os.path.dirname(__file__)) 
        print(f"Script Located In Directory: {script_path}")

        # Creates the output file for the script
        processed_file_path = Path(script_path) / "processed_output.txt"
        processed_file_path.touch()  
        print(f"Made File Named 'processed_output.txt' in {script_path}")

        # Creates the settings file for the project
        settings_file_path = Path(script_path) / "settings.txt"
        settings_file_path.touch()  
        print(f"Made File Named 'settings.txt' in {script_path}")


    def menu():
        startup_sequence()
        print("Start up completed!")
        while True :
            print ("1: Start")
            print ("2: Settings")
            print ("3: Exit")

            menu_input = input(("Please choose an option:  "))
            if (menu_input) == "1" or (menu_input.lower()) == "start":
                print("Starting Script")
                beautystall()
                output_converter_func()
            elif (menu_input) == "2" or (menu_input.lower()) == "settings":
                print("Settings")
                beautystall()
                settings_menu()
            elif (menu_input) == "3" or (menu_input.lower()) == "exit":
                print("Exiting Program!")
                beautystall()
                print("Output Converter Made By Mari! <3")
                beautystall()
                print("Hope it helped!")
                sys.exit()
            else :
                print ("Inccorect Option! Try Again!")
                beautystall()
    #settings menus
    def settings_menu():
        print("This is the settings menu!")
        beautystall()
        print("Here you can change all the variables of this AMAZING Script! ")
        beautystall()

        while True : 
            print ("1: Path")
            print ("2: TimeScale")
            print ("3: PersonalConfig")
            print ("4: FileName ")
            print ("5: Exit")

            settings_input = input("Please choose an option:  ")
            configvariable_input = ""
            if settings_input == "1" or  (settings_input.lower()) == "path":
                beautystall()
                print(f"Current path is set to {path}")
                print("Please make sure to put it to the directory and not the entire file path")
                beautystall()
                configvariable_input = input(str("Put your config here, if you want to keep it the same only hit enter: "))

            #settings for timescale, has a catch for if the user doesnt put a 0 or 1 and returns a value error and doesnt save 
            elif settings_input == "2" or (settings_input.lower()) == "timescale":
                beautystall()
                print(f"Current timescale is {timevariable}")
                beautystall()
                print("0 is the fastest, 1 is the longest <3")
                beautystall()
                try:
                    configvariable_input = input(str("Put your config here, if you want to keep it the same only hit enter: "))
                    if configvariable_input != 1 or 0 :
                        raise ValueError()
                except: 
                        beautystall()
                        print("The value has to be 0 or 1")
            #settings for the config list used mainly for automating the output as much as possible, have to enter it here like its a list format so use , between each object 
            elif settings_input == "3" or (settings_input.lower()) == "personalconfig":
                    beautystall()
                    print(f"Current Config is {personalconfig}")
                    beautystall()
                    print("You might wanna run the program at least once to know what the variables are <3")
                    beautystall()
                    configvariable_input = input(str("Put your config here, if you want to keep it the same only hit enter: "))

            #settings for output name, just a simple change of the default outputname for better automation again, gonna have it swap to the default if it detects that theres actually a change here
            #similar to the if statement I have now for the path at the top
            elif settings_input == "4" or (settings_input.lower()) == "filename":
                print("Change the output name here!")
                configvariable_input = input(str("Put your config here, if you want to keep it the same only hit enter: "))
                beautystall()
            

            elif (settings_input) == "5" or (settings_input.lower()) == "exit":
                print("Going back to the main menu! <3")
                beautystall()
                print("")
                print("")
                break

            else :
                print ("Inccorect Option! Try again!")
                beautystall()    
            #these two go very last and only ever trigger if configvariable is touched by any of the options above, if its not then the else statement above takes over!
            if len(configvariable_input) != 0:
                print("***********")
                print("Config saved!")
                print("***********")
                pass
                #write out to settings

            else: 
                print("***********")
                print("Config not saved!")
                print("***********")
                pass
                #dont write out


    #this is  the output coverter that takes the file and opens it, then reads it and takes the break in the txt file characters and make a dictionary out of them for more consistent or easier data manipulation
    def output_converter_func():
        x = 1 
        global path
        global outputfilename
        global personalconfig
        try:    
            if path != "default" : 
                print("Using Your Set Path")
                os.chdir (path)
                pass
            else:
                #DONT CHANGE THIS IN HERE, IT LITERALLY WONT WORK DUE TO THE IF STATEMENT ABOVE, CHANGE IT UP TOP WHERE ITS SUPPOSED TO GO YOU CREATURE 
                path = input("Please Put The Path Where The Input File Is Located: ")
                os.chdir (path)
                    
            
            if outputfilename != "default":
                print("Using the set File name")
                with open(outputfilename) as file:
                    beautystall()
                    lines = file.readlines()
               
            else : 
                outputfilename = input("No default file name set, please enter the file name along with the file extension! (File.Ext): ")
                with open(outputfilename) as file:
                    beautystall()
                    lines = file.readlines()
             
            for i in range(5):
                stupid_rotating_star=["*","**","***","****","*****"]
                print(f"Finding File :3 {stupid_rotating_star[i]} ")   
                beautystall()
            print("Found File!!")
            beautystall()
        except :
            print("File not found...")
            beautystall()
            print("***********") 
            raise ValueError (("Try checking set path or File Name :3"))             
            menu()
        
        for line in lines:
            
            x = x + 1 
            #unquote for troubleshootings
            #print(f"this is line number {x}")
            #print(f"this is what the line says {line}")

            line = line.strip().rstrip(',')
            #stops at a blank line
            if not line:
                continue
            #this is the break point between key and value for the dictionary, would have to be configured per data set, but so long as you have key : value this will be able to detect it very easily
            #but if your data set in the txt or csv file is like a - or a | you could change that here
            if ':' in line:
                #use this to strip unwanted things from the output, will make this into a customizable setting soon
                key, value = line.split(':', 1)
                key = key.strip().strip('"\'').lower()
                value = value.strip().strip('"\'').lower()
                data_dict[key] = value

        #unquote for troubleshooting dictionary output issues
        #print (f"this is the output!: {data_dict}")

        personalconfig_modified = personalconfig

        if personalconfig_modified != "default":
            print("Nice! Using Deafault Config!!")
            personalconfig_modified = personalconfig.split(",")
        else : 
            print("No config setup, Highly Reccomend if your using this more then once!")
            print(f"these are the known datapoints {data_dict.keys()}")
            beautystall()
            print("***********")
            beautystall()
            print("***********")
            personalconfig_input = input("Please input your configs in list format (score,exp,hp,time): ")
            personalconfig_modified = personalconfig_input.split(",")
            
        #uncomment for troubleshooting config settings
        #print(f"This is the Config Output: {personalconfig}")
        
        for words in personalconfig_modified:

            words = words.lower()
            words = words.strip()
            value = data_dict.get(words)
            if value is None:
                print(f"The Key {words} is not found, check spelling or config!")
            else:
                print(f"{words} : {value}")
                
        print("Thank You And Come Again!")


        
    #function that controls the little stops between some of the actions to make the UX a bit less jarring since this is a really light program
    def beautystall():
        time.sleep(timevariable)
    menu()

main()
