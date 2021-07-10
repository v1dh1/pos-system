#import statements
from Reports import Reports
from cashreg import cashRegMenu
import os 
class Menu:
#class controls entire POS 
    def menuRun():
        #controls the POS by giving the user a menu choice on what they want to do, is a static method
        #no parameters
        #no return 

        #menuExit is a boolean variable
        menuExit = True

        #while loop continues until menuExit is True 
        while menuExit:
            #user stores a string value of what they want to do 
            user = str(input('What would you like to do?\n1.Cash Register\n2.Inventory\n3.Exit system\nEnter: '))
            os.system('clear')
            #while loop ensures that the user enters a valid input 
            while user not in ['1','2','3']:
                #if user enters an invalid input, they must keep entering values until it is valid 
                user = str(input('Enter a valid option. What would you like to do?\n1.Cash Register\n2.Inventory\n3.Exit system\nEnter: '))
                os.system('clear')

            #end while 

            #if statement checks if the user chose 1 
            if user == '1':
                cashRegMenu.cashingOut()
            #end if 
                
            #elif checks if the user chose 2 
            elif user == '2':
                #mainList is an object of Reports class 
                Reports.reportmenu()
            #end elif 

            #elif the user chose 3 
            elif user == '3':
                #exit is an object of Reports class 
                print('You have chosen to exit\nGoodbye!')
                #calls exitAndPrint method to copy the inventory to a new file 
                Reports.exitAndPrint()
                #menuExit is True and program ends 
                menuExit = False
        #end while 

