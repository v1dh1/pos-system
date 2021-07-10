#import statements
from Reports import Reports
from Validate import Validate
import os

#cashire name 

class Payment:

    def __init__(self, paytype, amount):
        #function initialises paytype and amount
        #takes paytype and amount as parameters
        #no return 

        #if statement checks if paytype is 1, then self.paytype is debit
        if paytype == '1':
            self.paytype = 'Debit'

        #if statement checks if paytype is 2, then self.paytype is credit card
        elif paytype == '2':
            self.paytype = 'Credit Card'

        #if statement checks if paytype is 3, then self.paytype is cash
        elif paytype == '3':
            self.paytype = 'Cash'

        #self.amount stores a float
        self.amount = amount
    #end __init__


class Transaction:
#controls transactions 

    #listOfPayments stores an empty list
    listOfPayments = []
    
    def __init__(self, listofItems):
        #initalises listofItems
        #no parameters
        #no return
        self.listOfItems = listofItems
    #end __init__
    
    def computeSubtotal(self,quantity):
        #takes 1 parameter, quantity
        #calculates subtotal
        #returns the subtotal

        #subtotal stores a float
        #quantity is an integer stored as a string 
        #self.price is a float
        subtotal = int(quantity) * self.price
        return subtotal
    #end computeSubtotal()

    def computeTax(self, total):
        #takes 1 paramter, a float
        #calulates tax
        #returns tax
        TAXAMOUNT = 0.13
        #tax stores a float value
        tax = total * TAXAMOUNT
        return tax
    #end computeTax

    def computeTotal(self, total):
        #takes 1 paramter, a float
        #calculates final price
        #returns the final price

        #final stores a float 
        final = total * 1.13
        return final
    #end computeTotal()

    def takePayment(self, totalAmount):
        #takes 1 parameter, a float 
        #takes the customer's payment based on total price 
        #returns a list of payments

        #toBePaid stores a float 
        toBePaid = totalAmount
        #notPaid stores a boolean value 
        notPaid = True

        print(f'You currently owe ${toBePaid:.2f}')

        #while loop remains true until the user has payed atleast the final amount 
        while notPaid:
            #typePaid stores an integer
            typePaid = str(input('How are you going to pay?\n1.Debit\n2.Credit\n3.Cash\nEnter a number: '))

            #while loop validates typePaid input
            while typePaid not in ['1','2','3']:
                typePaid = str(input('\n\nTry again. How are you going to pay?\n1.Debit\n2.Credit\n3.Cash\nEnter a number: '))
            os.system('clear')
            #end while

            #paymentAmount stores a float input
            paymentAmount = str(input('How much are you paying with that method?\n$ '))
            os.system('clear')

            #paymentAmount gets validated as a float 
            paymentAmount = Validate.valFloat(paymentAmount)
            #paymentAmount now stores a float 
            paymentAmount = float(paymentAmount)
                
            #payment is an instance of Payment class
            payment = Payment(typePaid, float(paymentAmount))

            #if the payment amount is exactly what is to be paid, how the user paid and the amount paid are added to the list of payments
            if payment.amount == toBePaid:
                #change stores a float
                change = 0.00
                #listOfPayments is updated
                Transaction.listOfPayments.append([payment.paytype, payment.amount, change])
                #notPaid is now False
                notPaid = False
                cont = input('Press enter to continue: ')
                os.system('clear')
            #end if

            #if the user pays less than total price:
            elif payment.amount < toBePaid:
                
                #toBePaid stores a float with the amount user paid deducted from the total amount
                toBePaid -= paymentAmount

                #listOfPayments is now updated
                Transaction.listOfPayments.append([payment.paytype, payment.amount])
                cont = input('Press enter to continue: ')
                os.system('clear')

                print(f'You currently owe {toBePaid:.2f}')
            #end elif

            #if the user overpaid:
            elif payment.amount > toBePaid:
                #if statement makes sure user doesn't overpay with a credit card
                if payment.paytype == 'Credit Card':
                    print('\nYou cannnot overpay with a credit card, try again')
                #end if

                #else lets user overpay
                else:
                    #change stores a float of the change by subtracting the amount paid - the original total price
                    change = paymentAmount - toBePaid
                    #the listOfPayments get updated
                    Transaction.listOfPayments.append([payment.paytype, (payment.amount - change), change])
                    print(f'Your change is ${change:.2f}')
                    #notPaid is now false to end the payment process
                    notPaid = False
                    cont = input('Press enter to continue: ')
                    os.system('clear')
                #end else
            #end elif 
        #end while 
        return Transaction.listOfPayments
    #end takePayment()

class Item(Transaction):

    def __init__(self, name, price):
        #function initialises the class attributes
        #no paramters 
        #no return
        self.name = name
        self.price = price
    #end __init__()

    def getQuantity(self):
        #function gets the quantity of the items being bought 
        #stores a value called quantity 
        #returns the quantity 
        #quantity stores a string and is validated 
        quantity = str(input(f'How many of {self.name} are being bought?: '))
        quantity = Validate.isInteger(quantity)
        quantity = int(quantity)

        #for loop iterates through the inventory.txt
        for i in Reports.prodList:
            #if statement checks if the items are the same 
            if i.name == self.name:
                #while loop makes sure user doesn't enter a number that is over the current stock quantity 
                while int(i.qty) < int(quantity):
                    #quantity stores a string 
                    quantity = str(input(f'\nThere is not enough in stock. How many of {self.name} are being bought?: '))
                    quantity = Validate.isInteger(quantity)
                #end while 
            #end if 
        #end for  

        #for loop iterates through the prodict list and subtracts the quanitity once it's bought 
        for item in Reports.prodList:
            if item.name == self.name:
                item.qty -= int(quantity)
            #end if 
        #end for 
                
        return int(quantity)
    #end getQuantity()

    def __str__(self):
        #function uses dunder method to format a string 
        #returns a formatted string 
        #no paramters
        return f'{self.name} costs {self.price}'
    #end __str__ 



class Receipt(Transaction):

    #quantities list is an empty list, will store quantities of products in cart
    quantitiesList = []

    def getReceiptString(self, products):
        #takes 1 parameter, a list of products
        #gets the quantities from the list of products 
        #returns the quantitiesList, updated 
        #for loop iterates through the list 
        for i in products:
            #Gets the quantity by taking user input and adding it to the quantitiesList 
            Receipt.quantitiesList.append(i.getQuantity())
        #end for 
        return Receipt.quantitiesList
    #end getReceiptString()

    def printReceipt(self, products, cashier):
        #takes 2 parameters, a list of products and a string
        #prints the receipt based on the list 
        #no return 

        #count stores an integer 
        count = 0
        #totalCost stores an integer 
        totalCost = 0

        #while loop iterates until count has reached the length of products 
        while count != len(products):
            #output stores an empty string 
            output = ''
            #for loop iterates through products 
            for i in products:
                #output now stores the main line of the receipt where an item's quantity, name and total price are all printed out 
                output += f'{Receipt.quantitiesList[count]:<10}{i.name:<35}${(i.computeSubtotal(Receipt.quantitiesList[count])):.2f}\n'

                #totalCost stores a float which is calculated by calculating the subtotal for every item, then adding it all to totalCost
                totalCost += i.computeSubtotal(Receipt.quantitiesList[count])
                count += 1
            #end for
        #end while 

        #itemExample stores an instance of item class 
        itemExample = Item('example',0)

        #finalMoney stores a float (the total cost of the cart)
        finalMoney = itemExample.computeTotal(totalCost)
        #payments stores a listOfPayments of how the user payed for their cart
        payments = itemExample.takePayment(finalMoney)

        #print statements for receipt 
        print('*'*50)
        print('Vidhi Grocery')
        print('*'*50)
        print(f'{"Cashier:":10}{cashier}')
        print('*'*50)
        print(f'{"Quantity":10}{"Item":<35}{"Price":<10}')
        print(output)
        print('*'*45)     
        print(f'{"Subtotal":<45}${totalCost:.2f}')   
        print(f'{"Tax":<45}${itemExample.computeTax(totalCost):.2f}')
        header = print(f'{"==":30}')
        print(f'{"Total":45}${finalMoney:.2f}')
        #for loop iterates through payments to print out the method and amount the user payed 
        for i in payments:
            print(f'{i[0]:<44} -{i[1]:.2f}')
        #end for
        #change stores the amount the user overpaid by, as a float
        print()
        #change stores an integer 
        change = payments[-1][2]
        print(f"{'Your change is':<44} ${change:.2f}")
        print(f'{"Balance":<45}${"0.00"}')
        print('Have a nice day!')
        #asking user to keep going and clears the screen 
        cont = input('\n\nPress anything to continue: ')
        os.system('clear')

    #end printReceipt()
#end Receipt class

class cashRegMenu:
#main class of cash register, controls the order in which things happen

    def cashingOut():
        #takes no parameters
        #runs while the user is cashing out their cart 
        #no return 

        #start is an empty input, just to continue with the process 
        start = input('\nPress anything to start a purchase\n')

        cashier = str(input('Enter your name: '))

        os.system('clear')

        #buying stores a boolean value to control a while loop 
        buying = True

        #cart is an empty list, will contain products that the user is buying 
        cart = []

        #while loop is true while user is purchasing items 
        while buying:

            #userItem stores a string of the SKU of the product being bought 
            userItem = str(input('Enter the SKU of the item being bought: ')).upper()

            #allItems stores an empty list 
            allItems = []
            #for loop checks adds all product SKUs to allItems list 
            for i in Reports.prodList:
                allItems.append(i.sku)
            #end for 
            #while loop checks if userItem is valid 
            while userItem not in allItems:
                #user enters item SKU until it is valid 
                userItem = str(input('\nThat item does not exist. Enter the SKU of the item being bought: ')).upper()
            #end while 

            #for loop goes through the inventory.txt file 
            for item in Reports.prodList:
                #if statment checks if the item sku is in the file 
                if item.sku in userItem:
                    #tempItem is an instance of the item class 
                    tempItem = Item(item.name, item.currentPrice)
                    #product gets added to the cart
                    cart.append(tempItem)
                #end if 
            #end for 

            #keepBuying asks user if another item is being bought, stores a string 
            keepBuying = str(input('Purchase another product?: Enter n for no, anything else for yes: '))
            cont = input('Press enter to continue: ')
            os.system('clear')

            #if user says no, cart stops being updated and code proceeds to make a receipt
            if keepBuying == 'n':
                #buying is False to exit the loop
                buying = False
            #end if 
        #end while 

        #run is an instance of Receipt
        run = (Receipt(cart))
        #getting the receipt 
        print(run.getReceiptString(cart))
        #printing is out 
        print(run.printReceipt(cart, cashier))

        return 
    #end cashingOut()

#end cashRegMenu
    