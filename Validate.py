class Validate:
#has methods used to validate values 
    def isInteger(val):
        #validates an integer
        #takes a value as a parameter 
        #returns back the value (an integer)

        #while loop checks if the value is numeric 
        while val.isnumeric() == False:
            #val asks user to input again if it isn't 
            val = str(input('Not valid. Try again: '))
        #end while 
        
        #while loop ensures the number is over 0 
        while int(val) < 0:
            val = str(input('Try again: '))
        #end while 

        return val
    #end isInteger

    def isFloat(value):
        #isFloat checks if a value is a float 
        #takes a value as a parameter 
        #returns a boolean Value 

        #tries to see if the value can be a float, if yes returns true 
        try:
            float(value)
            return True
        #end try 

        #if there is a value error then it is not a float and returns false 
        except ValueError:
            return False
        #end Except  
    #end isFloat()

    def valFloat(value):
        #validates a float 
        #takes a value as a parameter 
        #returns a float

        #while loop runs until the user enters a float 
        while Validate.isFloat(value) != True:
            value = input('enter again: ')
        #end while 
        
        #while loop runs until the number is above 0 
        while float(value) < 0:
            value = input('enter again: ')
        #end while 
        
        return value
    #end valFloat()
    
    def valStrAsNum(validInputs, userInput):
        #validates a string as an integer 
        #returns an integer 
        #takes 2 parameters: a list of acceptable values and a userInput 

        #while loop runs until the user enters a value that is in the list 
        while userInput not in validInputs:
            #userInput stores a string 
            userInput = str(input('Try that again: '))
        #end while 
        return userInput
    #end valStrAsNum

    def valCategory(userInput):
        #validates a category 
        #takes in a string as a parameter 
        #returns a string 

        #while loop runs until user enters an element in the list 
        while userInput not in ['VEG', 'FRU', 'MEA', 'OTH']:
            #userInput stores a string input 
            userInput = str(input('Enter that again: ')).upper()
        #end while 
        return userInput
    #end valCategory

    def valCtgy(user):
        #validates a category 
        #takes in a string as a parameter 
        #returns a string 

        #while loop runs until user enters an element in the list
        while user not in ['VEG', 'FRU', 'MEA', 'OTH']:
            #user stores a string input 
            user = str(input('Enter that again: ')).upper()
        #end while 

        #fullWord is a dictionary 
        fullWord = {'VEG':'VEGETABLE', 'FRU':'FRUIT','MEA':'MEAT','OTH':'OTHER'}

        #for loop finds the user input in the dictionary and returns the full version of the word 
        for key in fullWord:
            if user == key:
                return fullWord[key]
            #end if 
        #end for 
    #end valCtgy()