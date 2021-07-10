#import statements 

from Product import Product
import datetime
import pytz
from Validate import Validate
import os

class PrintingOut:
#controls large outputs to only display 24 lines at a time 

    #maxOutput stores an integer of amount of lines per page
    maxOutput = 24
    #lines counts the lines 
    lines = 1
    #cont stores a string 
    cont = '\nPress enter for next page\n'

    def __init__(self, numLines):
        #initialises numLines (an integer)
        #no returns 
        #no parameters 
        self.numLines = numLines
    
    def updateCounter(self):
        #updates the counter by adding 1 per line 
        #no return 
        #no parameters
        #self.numLines gets updated as lines get run through 
        self.numLines += self.lines
        #if there has been 24 lines, then the message is printed 
        if self.numLines % self.maxOutput == 0:
            input(self.cont)
        #end if 

        return

class mainList:
#has a method which gets the mainList of products 
    def getList():
        #takes no paramters  
        #creates a list of all items in a file 
        #returns the list 

        #prods stores an empty list 
        prods = []
        #opening a file to read 
        with open('inventory.txt', 'r') as f:
            #for loop iterates through line in the file 
            for line in f:
                #data replaces spaces with commas  
                data = line.replace('\n','').split(',')
                #item is an instance of Product
                item = Product(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
                #adds the item object to prods list 
                prods.append(item)
        #returns the prods list 
        return prods
    #end getList()    

class Reports:
#manages entire inventory

    #getting the main product list
    prodList = mainList.getList()

    def allSku():
        #no parameters
        #gets a list of skus from the prodlist
        #returns this list 

        #skuList stores a list, initially empty
        skuList = []
        #for loop iterates through prodList 
        for i in Reports.prodList:
            #adding the skus to the skuList
            skuList.append(i.sku)
        #end for 
        return skuList
    #end allSku

    def allNames():
        #no parameters
        #gets a list of product names from the prodlist
        #returns this list 

        #nameList stores a list, initially empty
        nameList = []
        #for loop iterates through prodList 
        for i in Reports.prodList:
            #adding the skus to the nameList
            nameList.append(i.name)
        #end for 
        return nameList
    #end allNames

    def reportsBasedOnCategory():
        #prints out a report of items based on category
        #no parameters 
        #no returns 

        #userCtgy gets user input on a category and is validated as a string
        userCtgy = str(input('Enter the category type (first 3 letters): ')).upper()
        userCtgy = Validate.valCategory(userCtgy)

        os.system('clear')

        print(f"{'Item': <10}{'Name': <21}{'Category': <10}{'Qty': <10}{'R. Qty' : <10}{'Price': <11}{'Sale': <10}Profit")
        #controlLines is an object of PrintingOut
        controlLines = PrintingOut(0)
        #for loop iterates through the product list 
        for item in Reports.prodList:
            #if the category is in the item's category 
            if userCtgy in item.ctgy:
                #the profit stores a formatted string 
                profit = f'{item.profit:.02f}'
                controlLines.updateCounter()
                #controlLines calls update counter method to ensure that lines are only printed 24 at a time 
                #prints out the item is a formatted way 
                print(f"{item.sku: <10}{item.name[:20]: <21}{item.ctgy: <10}{item.qty: <10}{item.rqty: <10}${(float(item.vendorPrice)): <10.2f}${float(item.currentPrice): <10.2f}${float(profit): <10.2f}")
            #end if 
        #end for 
        return
    #end reportsBasedOnCategory()

    def reportsBasedOnQuantity():
        #prints out a report based on quantity 
        #no parameters 
        #no returns 

        #userQuan stores a string which is an integer and is validated 
        userQuan = str(input('Enter a minimum quantity you want to see products under: '))
        userQuan = Validate.isInteger(userQuan)
        #prints out a header 
        print(f"{'Item': <10}{'Name': <21}{'Category': <10}{'Qty': <10}{'R. Qty' : <10}{'Price': <11}{'Sale': <10}Profit")
        #controlLines is an object of PrintingOut
        controlLines = PrintingOut(0)
        #for loop iterates through the product list 
        for item in Reports.prodList:
            #if the category is in the item's category 
            if int(userQuan) > int(item.qty):
                #the profit stores a formatted string 
                profit = f'{item.profit:.02f}'
                #controlLines calls update counter method to ensure that lines are only printed 24 at a time 
                controlLines.updateCounter()
                #prints out the item is a formatted way 
                print(f"{item.sku: <10}{item.name[:20]: <21}{item.ctgy: <10}{item.qty: <10}{item.rqty: <10}${(float(item.vendorPrice)): <10.2f}${float(item.currentPrice): <10.2f}${float(profit): <10.2f}")
            #end if 
        #end for 
        return
    #end reportsBasedOnQuantity()

    def generalReport():
        #prints out a report of all items in stock 
        #no parameters 
        #no returns 

        #prints out header 
        print(f"{'Item': <10}{'Name': <21}{'Category': <10}{'Qty': <10}{'R. Qty' : <10}{'Price': <11}{'Sale': <10}Profit")
        #controlLines is an object of PrintingOut
        controlLines = PrintingOut(0)
        #for loop iterates through the product list 
        for item in Reports.prodList:
            #the profit stores a formatted string 
            profit = f'{item.profit:.02f}'
            #controlLines calls update counter method to ensure that lines are only printed 24 at a time 
            controlLines.updateCounter()
            #prints out the item is a formatted way 
            print(f"{item.sku: <10}{item.name[:20]: <21}{item.ctgy: <10}{item.qty: <10}{item.rqty: <10}${(float(item.vendorPrice)): <10.2f}${float(item.currentPrice): <10.2f}${float(profit): <10.2f}")
        #end for 
        return
    #end generalReport()


    def getReport():
        #no parameters
        #returns null 
        #gets reports based on what user wants (acts as a menu)

        #clears screen 
        os.system('clear')

        #reportType stores a string of user input 
        reportType = str(input('Would you like a report based on:\n1.Category\n2.Quantity\n3.All Items\nEnter a number: '))
        print()
        #validates the reportType
        reportType = Validate.valStrAsNum(['1','2','3'],reportType)
        #if/elif/elif prints out a report based on user input by calling appropriate methods 
        if reportType == '1':
            Reports.reportsBasedOnCategory()
        #end if

        elif reportType == '2':
            Reports.reportsBasedOnQuantity()
        #end elif
            
        elif reportType == '3':
            Reports.generalReport()
        #end elif 

        #asks user to enter anything and then clears the screen 
        cont = input('Enter anything to continue: ')
        os.system('clear')

        return
    #end getReport()

    def addQuantityBasedOnSku():
        #adds stock to a specific item 
        #no parameters 
        #no return 

        #userSku stores a string of a sku and is validated 
        userSku = str(input('Enter the SKU of the item: ')).upper()
        while userSku not in Reports.allSku():
            userSku = str(input('Try again: ')).upper()
        #end while 
        
        #toAdd stores a string which is an integer and validates it 
        toAdd = str(input('Enter a quantity to add: '))
        toAdd = Validate.isInteger(toAdd)

        #for loop iterates through the main list of products 
        for i in Reports.prodList:
            #when the item is found the toAdd value is added to the current stock 
            if userSku == i.sku:
                oldQuan = i.qty
                i.qty += int(toAdd)
                print(f'\n{i.name} has been updated from {oldQuan} to {i.qty}\n')
            #end if 
        #end for 
    #end addQuantityBasedOnSku()

    def addQuantityBasedOnStock():
        #adds quantity based on a stock amount 
        #no parameter 
        #no returns 

        #valueUnder stores a string of an integer and validates it 
        valueUnder = str(input('What is the minimum stock value you are looking for products under: '))
        valueUnder = Validate.isInteger(valueUnder)

        #valueToAdd is a string that stores an integer and is validated 
        valueToAdd = str(input('How much stock would you like to add to those items: '))
        valueToAdd = Validate.isInteger(valueToAdd)


        #for loop iterates through the product list 
        for item in Reports.prodList:
            #finds the items which are under the minimum stock 
            if item.qty < int(valueUnder):
                #adds the value to add to the quantity 
                item.qty += int(valueToAdd)
            #end if 
        #end for 

        return
    #end addQuantityBasedOnStock

    def addQuantityBasedOnWarning():
        #adds a quantity based on an item warning 
        #no parameters 
        #no returns 

        #stockToAdd stores a string of an integer and validates it 
        stockToAdd = str(input('What amount of stock would you like to add to items with a low stock warning?: '))
        stockToAdd = Validate.isInteger(stockToAdd)

        #for loop iterates through the product list 
        for i in Reports.prodList:
            #if the warning is true then the item has stock added to it 
            if i.warning == True:
                i.qty += int(stockToAdd)
            #end if 
        #end for 
        print('Items have been restocked.')
        return 
    #end addQuantityBasedOnWarning()

    
    def addQuantity():
        #acts as a menu for the user to add quantity 
        #no parameters
        #no return 

        #clearing the screen 
        os.system('clear')

        #userAdds stores a string of the user's input 
        userAdds = str(input('Would you like to add quantity to:\n1.A specific item\n2.A batch based on quantity\nEnter: '))
        #validates the input 
        userAdds = Validate.valStrAsNum(['1','2'],userAdds)
        #if/elif calls methods based on what the user wants to do 
        if userAdds == '1':
            Reports.addQuantityBasedOnSku()
        #end if 
        elif userAdds == '2':
            #userAddsValue stores a string which is the user input and validates it 
            userAddsValue = str(input('Would you like to add a quantity based on:\n1.Value\n2.Warning\nEnter: '))
            userAddsValue = Validate.valStrAsNum(['1','2'],userAddsValue)

            #if/elif calls methods based on what the user wants to do 
            if userAddsValue == '1':
                Reports.addQuantityBasedOnStock()
            #end if 
            
            elif userAddsValue == '2':
                Reports.addQuantityBasedOnWarning()
            #end elif 

        #asks user to press anything and then clears the screen 
        cont = input('Enter anything to continue: ')
        os.system('clear')

        return
    #end addQuantity

    def deleteItem():
        #deletes an item 
        #no paramters
        #no returns 

        #clears the screen 
        os.system('clear')
        #userDeletes stores a string of the sku and validates it 
        userDeletes = str(input('Enter the SKU of the item you want to remove: ')).upper()
        #if the sku did not exist:
        while userDeletes not in Reports.allSku():
            userDeletes = str(input('Try again: ')).upper()
        #end while 
        os.system('clear')
        #asks user to confirm deletion 
        confirmDelete = input(f'Are you sure you want to delete item {userDeletes}? Press enter to continue.')
        #for loop iterates though the product list 
        for i in Reports.prodList:
            #finds the item and then deletes the item 
            if userDeletes == i.sku:
                Reports.prodList.remove(i)
            #end if 
        #end for 

        #prints out message 
        print(f'Item {userDeletes} has been removed.')
        #asks user to continue and then clears the screen 
        cont = input('Enter anything to continue: ')
        os.system('clear')
    #end deleteItem()
        

    def addItem():
        #adds an item 
        #no parameters 
        #no return 

        #clears screen and prints a message 
        os.system('clear')
        print('You chose to add an item')
        #newName gets a new name for the item 
        newName = str(input('Enter a name for the new product: '))
        #newCtgy gets user input on a category and is validated as a string
        newCtgy = str(input('Enter the category of the new product: ')).upper()
        newCtgy = Validate.valCtgy(newCtgy).upper()
        #newQty gets a new quantity for the item and validates it 
        newQty = str(input('Enter the regular stock of the item: '))
        newQty = Validate.isInteger(newQty)
        #newRQty is set as the quantity 
        newRQty = newQty
        #newVendorPrice is a string, asking for user input and validating it 
        newVendorPrice = str(input('Enter the vendor price: '))
        newVendorPrice = Validate.valFloat(newVendorPrice)
        #newMarkUpPercentage is a string, asking for user input and validating it 
        newMarkUpPercentage = str(input('Enter a mark up percentage as a whole number: '))
        newMarkUpPercentage = float(Validate.valFloat(newMarkUpPercentage))
        #newRegPrice is calculated by multiplying the vendor price by the mark up percentage 
        newRegPrice = float(newVendorPrice) * (1+((newMarkUpPercentage)/100))
        #newDicountPercent is a string, asking for user input and validating it 
        newDicountPercent = str(input('Enter a new discount percent as a whole number: '))
        newDiscountPercent = Validate.valFloat(newDicountPercent)
        newCurrentPrice = float(newRegPrice) * ((100-(float(newDicountPercent)))/100)
        #ctgyList is an empty list 
        ctgyList  = []
        #for loop iterates through the product list 
        for item in Reports.prodList:
            #adds the item's sku to the ctgyList 
            if newCtgy in item.ctgy:
                ctgyList.append(item.sku)
            #end if 
        #end for 
        #newSku is a SKU 
        newSku = int(ctgyList[-1][4:]) + 1
        #int(ctgyList[-1][4:]) +1
        print(newSku)
        #newSku is formatted 
        newSku = f'{(newCtgy[:3])}-{newSku:04d}'
        #newItem is an instance of Product class 
        newItem = Product(newSku, newName, newCtgy, newQty, newRQty, newVendorPrice, newMarkUpPercentage, newRegPrice, newDiscountPercent, newCurrentPrice)
        #adding the new item to the main list 
        Reports.prodList.append(newItem)
        #prints out the header 
        print(f"{'Item': <10}{'Name': <21}{'Category': <10}{'Qty': <10}{'R. Qty' : <10}{'Price': <11}{'Sale': <10}Profit")
        for item in Reports.prodList:
            #if the category is in the item's category 
            if item.sku == newItem.sku:
                #the profit stores a formatted string 
                profit = f'{item.profit:.02f}'
                #controlLines calls update counter method to ensure that lines are only printed 24 at a time 
                #prints out the item is a formatted way 
                print(f"{item.sku: <10}{item.name[:20]: <21}{item.ctgy[:3]: <10}{item.qty: <10}{item.rqty: <10}${(float(item.vendorPrice)): <10.2f}${(float(item.currentPrice)): <10.2f}${(float(profit)): <10.2f}")
            #end if 
        #end for 
        #asks user to continue and then clears the screen 
        cont = input('\n\nEnter anything to continue: ')
        os.system('clear')
        return 
    #end addItem()

    def printOutToModifyDetails(toModify):
        #prints out details of a modified item 
        #takes 1 parameter: an item which was modified 
        #no return 

        #prints out header 
        print('Product Details:\n')
        print(f"{'Item': <10}{'Name': <21}{'Category': <10}{'Qty': <10}{'R. Qty' : <10}{'Price': <11}{'Sale': <10}Profit")
        #for loop iterates though the product list 
        for item in Reports.prodList:
            #when the item is found, it is printed out and modified 
            if item.sku == toModify:
                profit = f'{item.profit:.02f}'
                print(f"{item.sku: <10}{item.name[:20]: <21}{item.ctgy: <10}{item.qty: <10}{item.rqty: <10}${(float(item.vendorPrice)): <10.2f}${float(item.currentPrice): <10.2f}${float(profit): <10.2f}\n\n")
            #end if 
        #end for 
        return
    #end printOutToModifyDetails()

    def modifyVendorPrice(toModify):
        #modifies the vendor price 
        #no returns 
        #takes 1 parameter: a sku of an item which needs to be modified 

        #newSetVendorPrice stores a user input as a string and validates it 
        newSetVendorPrice = str(input('Enter a new vendor price: '))
        newSetVendorPrice = Validate.valFloat(newSetVendorPrice)
        #for loop iterates through all the items in the product list 
        for i in Reports.prodList:
            #if the item is found then a new vendor price is calulated
            if toModify == i.sku:
                newVenPrice = newSetVendorPrice
                regPrice = float(newVenPrice) * (1 + float(i.markUpPercent)/100)
                #if it is below 0, it does not allow it to change 
                if regPrice < 0:
                    print('Setting this vendor price would let the profit be below 0.')
                #end if 
                else:
                    #it allows it to change if the profit isn't under 0 
                    i.vendorPrice = newSetVendorPrice
                    i.regPrice = float(i.vendorPrice) * (1 + float(i.markUpPercent)/100)
                    i.currentPrice = float(i.regPrice) * (100 - float(i.salePercent)/100)
                #end else 
            #end for 
        #asks user to continue and clears the screen 
        cont = input('\n\nEnter anything to continue')
        os.system('clear')
        return 
    #end modifyVendorPrice()

    def modifyMarkUpPercentage(toModify):
        #method modifies a mark up percentage 
        #no parameters 
        #no returns 
        os.system('clear')

        #newSetMarkUpPercentage stores a string of user input and validates it 
        newSetMarkUpPercentage = str(input('What would you like to change the mark up percentage to?: '))
        newSetMarkUpPercentage = Validate.valFloat(newSetMarkUpPercentage)
        #for loop iterates through the product list and modifies it's values 
        for i in Reports.prodList:
            if toModify == i.sku:
                #the mark up percent gets modified along with it's regular price, mark up percent and current price 
                i.markUpPercent = newSetMarkUpPercentage
                i.regPrice = float(i.vendorPrice) * (1 + float(i.markUpPercent)/100)
                i.currentPrice = float(i.regPrice) * (100 - float(i.salePercent)/100)
            #end if 
        #end for 

        #asks user to continue and clears the screen 
        cont = input('\n\nEnter anything to continue')
        os.system('clear')
        return 
    #end modifyMarkUpPercentage

    def modifyMinQuantity(toModify):
        #no parameters
        #no returns 
        #modifies an items quantity

        #clears the screen 
        os.system('clear')

        #newRQty asks the user for an input and stores a string, gets validated 
        newRQty = str(input('Enter a new regular quantity: '))
        newRQty = Validate.isInteger(newRQty)

        #for loop iterates through the profuct list 
        for i in Reports.prodList:
            #when the item is found, it's regular quantity gets replaced 
            if toModify == i.sku:
                i.rQty = newRQty
            #end if 
        #end for 

        print('\nRegular Quantity has been modified')
        #asks user to continue and clears the screen 
        cont = input('\n\nEnter anything to continue')
        os.system('clear')

        return 
    #end modifyMinQuantity()
        


    def modify():
        #no parameters
        #no returns 
        #modifies an item 

        #clears a screen 
        os.system('clear')
        #toModify stores a string and gets user input 
        toModify = str(input('Enter the SKU of the item you want to modify: ')).upper()
        #validates toModify 
        while toModify not in Reports.allSku():
            toModify = str(input('Enter that again: ')).upper()
        #end while 

        os.system('clear')
        #prints out the item details 
        Reports.printOutToModifyDetails(toModify)
        #elementMod stores a string and gets user input and validates it 
        elementMod = str(input('Would like you to mofify\n1.Name\n2.Vendor Price\n3.Mark Up Percentage\n4.Sale Percentage\n5.Minimum required items\nEnter a number: '))
        elementMod = Validate.valStrAsNum(['1','2','3','4','5'], elementMod)
        #if the user chose to change the name
        if elementMod == '1':
            #newSetname stores a string of the name 
            newSetName = str(input('Enter a new name for the product: '))
            #for loop iterates through the product list and switches the name 
            for i in Reports.prodList:
                if toModify == i.sku:
                    i.name = newSetName
                #end if 
            #end for 
        #end if 

        elif elementMod == '2':
            #calls modifyVendorPrice method 
            Reports.modifyVendorPrice(toModify)
        #end elif 
            
        elif elementMod == '3':
            #calls modifyMarkUpPercentage method 
            Reports.modifyMarkUpPercentage(toModify)
        #end elif 

        elif elementMod == '4':
            #newSetSalePercentage stores a string of the user input and validates it 
            newSetSalePercentage = str(input('What would you like to change the sale percentage to?: '))
            newSetSalePercentage = Validate.valFloat(newSetSalePercentage)
            #for loop finds the product in the product list and modifies it's values 
            for i in Reports.prodList:
                if toModify == i.sku:
                    i.salePercent = newSetSalePercentage
                    i.currentPrice = float(i.regPrice) * (100 - float(i.salePercent)/100)
                #end if 
            #end for 
        #end elif 

        elif elementMod == '5':
            Reports.modifyMinQuantity(toModify)
        #end elif 

        #asks user to continue and clears the screen 
        cont = input('\n\nEnter anything to continue: ')
        os.system('clear')
        return
    #end modify()

            

    def searchBySku():
        #no parameters
        #no return 
        #searches an item by it's sku 

        #clears screen 
        os.system('clear')

        #itemToSearch stores a string of user input 
        itemToSearch = str(input('Enter the sku of the item you want to search: ')).upper()
        #validates the itemToSearch
        while itemToSearch not in Reports.allSku():
            itemToSearch = str(input('Try that again: ')).upper()
        #end while 
        for item in Reports.prodList:
            #finds the item and prints it out 
            if itemToSearch == item.sku:
                print(f"{'Item': <10}{'Name': <21}{'Category': <10}{'Qty': <10}{'R. Qty' : <10}{'Price': <11}{'Sale': <10}Profit")
                #the profit stores a formatted string 
                profit = f'{item.profit:.02f}'
                #controlLines calls update counter method to ensure that lines are only printed 24 at a time 
                #prints out the item is a formatted way 
                print(f"{item.sku: <10}{item.name[:20]: <21}{item.ctgy: <10}{item.qty: <10}{item.rqty: <10}${(float(item.vendorPrice)): <10.2f}${float(item.currentPrice): <10.2f}${float(profit): <10.2f}")
            #end if 
        #end for 
        #asks user to continue and clears the screen 
        cont = input('\n\nEnter anything to continue: ')
        os.system('clear')
    #end searchBySku()

    def searchByName():
        #no parameters
        #no returns 
        #searches for an item by it's name 

        #clears the screen 
        os.system('clear')

        #nameToSearch stores a string of user input and validates it 
        nameToSearch = str(input('Enter the name of the item you want to find: ')).title()
        while nameToSearch not in Reports.allNames():
            nameToSearch = str(input('Enter the name of the item you want to find: '))
        #end while 
        #finds the item in the product list and prints it out 
        for item in Reports.prodList:
            if nameToSearch == item.name:
                print(f"{'Item': <10}{'Name': <21}{'Category': <10}{'Qty': <10}{'R. Qty' : <10}{'Price': <11}{'Sale': <10}Profit")
                #the profit stores a formatted string 
                profit = f'{item.profit:.02f}'
                #controlLines calls update counter method to ensure that lines are only printed 24 at a time 
                #prints out the item is a formatted way 
                print(f"{item.sku: <10}{item.name[:20]: <21}{item.ctgy: <10}{item.qty: <10}{item.rqty: <10}${(float(item.vendorPrice)): <10.2f}${float(item.currentPrice): <10.2f}${float(profit): <10.2f}")
            #end if 
        #end for 

        #asks user to continue and clears the screen 
        cont = input('\n\nEnter anything to continue: ')
        os.system('clear')
        return 
    #end searchByName()

    def saleByCategory():
        #puts a category on sale 
        #no parameters 
        #no returns 

        #clears screen 
        os.system('clear')
        #ctgyOnSale stores a string and validates it 
        ctgyOnSale = str(input('Enter the category you want to put on sale (first 3 letters): ')).upper()
        ctgyOnSale = Validate.valCtgy(ctgyOnSale)

        #asks for a new sale percent and validates it 
        newSalePercentage = str(input('Enter a new sale percentage: %'))
        newSalePercentage = Validate.valFloat(newSalePercentage)
        #control lines is called to ensure that lines are spaced at 24
        controlLines = PrintingOut(0)
        #notOnSale stores an empty string 
        notOnSale = []
        for item in Reports.prodList:
            #finds the item in the product list 
            if item.ctgy == ctgyOnSale:
                #sets new profit price by subtracting the current price by the sale percenatge 
                newProfitPrice = float(item.currentPrice) - (float(item.currentPrice) * float(newSalePercentage)/100)
                #profit stores an integer
                profit = newProfitPrice - float(item.vendorPrice)
                
                #if the profit is less than 0 the item is not put on sale and is added to the notOnSale list 
                if profit < 0:
                    notOnSale.append(item.name)
                #end if 
                else:
                    #otherwise the product's values are changed accordingly 
                    item.salePercent = newSalePercentage
                    item.currentPrice = newProfitPrice
                    item.profit = profit  
                #end else 
            #end if 
        #end for 

        #printing the things that were not put on sale 
        print(f'Items that were not able to be put on sale:\n{notOnSale}')
        controlLines.updateCounter()

        #asks user to continue and then clears the screen 
        cont = input('\n\nEnter anything to continue: ')
        os.system('clear')
        return
    #end saleByCategory()

    def saleBySku():
        #puts an item on sale by it's sku 
        #no parameters 
        #no returns 

        #clears the screen 
        os.system('clear')
        #skuOnSale stores a string which gets user input and validates it 
        skuOnSale = str(input('Enter the SKU of the item being placed on sale: ')).upper()
        while skuOnSale not in Reports.allSku():
            skuOnSale = str(input('Try again: ')).upper()
        #end while 

        #newSalePercentage stores a string and validates it 
        newSalePercentage = str(input('Enter a new sale percentage: %'))
        newSalePercentage = Validate.valFloat(newSalePercentage)

        #for loop iterates through the product list 
        for item in Reports.prodList:
            #when it finds the item:
            if skuOnSale == item.sku:
                #the new profit price is calculated by mutiplying the current price by the new sale percentage 
                newProfitPrice = float(item.currentPrice) - (float(item.currentPrice) * float(newSalePercentage)/100)
                #the profit is calulated 
                profit = float(newProfitPrice) - float(item.vendorPrice)
                #if the profit is less than 0 then it's price is not updated 
                if profit < 0:
                    print('\nThat sale percentage is too low.')
                #end if 
                else:
                    #if it is not too low, then it's updated
                    item.salePercent = newSalePercentage
                    item.currentPrice = newProfitPrice
                    item.profit = profit  
                    print('\nSale percent has been updated')
                #end else 
            #end if 
        #end for 

        #asks user to continue and clears the screen 
        cont = input('\n\nEnter anything to continue: ')
        os.system('clear')
        return 
    #end saleBySku()


    def putAnItemOnSale():
        #puts an item on sale 
        #no parameters 
        #no returns 

        #clears screen 
        os.system('clear')
        #saleMethod acts as a menu for the user , stores a string which is validated 
        saleMethod = str(input('Would you like to place items on sale based on \n1.Category\n2.SKU\nEnter: '))
        #while loop validates saleMethod
        while saleMethod not in ['1','2']:
            saleMethod = str(input('Invalid, try again. Would you like to place items on sale based on \n1.Category\n2.SKU\nEnter: '))
        #end while 
        #calls methods based in what the user chose 
        #if the user chose 1
        if saleMethod == '1':
            Reports.saleByCategory()
        #end if 

        elif saleMethod == '2':
            Reports.saleBySku()
        #end elif 
    #end putAnItemOnSale()

    def removeSaleBySku():
        #removes the sale on an item 
        #no parameters 
        #no returns 

        #clears screen 
        os.system('clear')

        #skuNotOnSale stores a string of a sku which is getting it's sale removed and is validated 
        skuNotOnSale = str(input('Enter the SKU of the item being placed on sale: ')).upper()
        while skuNotOnSale not in Reports.allSku():
            skuNotOnSale = str(input('Try again: ')).upper()
        #end while 

        #newSalePercentage stores an integer 
        newSalePercentage = 0

        #for loop iterates through the product list and tries to find the item 
        for item in Reports.prodList:
            #once it is found, it removes it's sale 
            if skuNotOnSale == item.sku:
                #it's elements are set back to an unsale amount 
                item.salePercent = newSalePercentage
                item.currentPrice = (item.regPrice)
        #prints out message 
        print('Sale has been removed.')

        #asks user to continue and clears the screen 
        cont = input('\n\nEnter anything to continue: ')
        os.system('clear')
        return 
    #end removeSaleBySku


    def removeSaleByCategory():
        #removes the sale of an entire category 
        #no parameters 
        #no returns 

        #clears the screen 
        os.system('clear')
        #ctgyOnSale stores a string and is validated 
        ctgyNotOnSale = str(input('Enter the category you want to put on sale (first 3 letters): ')).upper()
        ctgyNotOnSale = Validate.valCtgy(ctgyNotOnSale)

        #newSalePercentage stores an integer 
        newSalePercentage = 0

        #for loop iterates through the product list 
        for item in Reports.prodList:
            #once it finds an item of that category it sets it sale percent to 0 and updates the current price 
            if ctgyNotOnSale == item.ctgy:
                item.salePercent = newSalePercentage
                item.currentPrice = (item.regPrice)
            #end if 
        #end for 

        #prints out message 
        print('Sale has been removed')

        #asks user to continue and clears screen 
        cont = input('\n\nEnter anything to continue: ')
        os.system('clear')
        return 
    #end removeSaleByCategory



    def removeSale():
        #removes sale : acts as a menu 
        #no parameters 
        #no returns 

        #clears screen 
        os.system('clear')

        #removeSaleMethod stores a string of the user input 
        removeSaleMethod = str(input('Would you like to remove items on sale based on \n1.Category\n2.SKU\nEnter: '))
        #while loop validates saleMethod
        while removeSaleMethod not in ['1','2']:
            removeSaleMethod = str(input('Invalid, try again. Would you like to place items on sale based on \n1.Category\n2.SKU\nEnter: '))
        #end while 

        #if and elif call methods based on user input 
        if removeSaleMethod == '1':
            Reports.removeSaleByCategory()
        #end if 

        elif removeSaleMethod == '2':
            Reports.removeSaleBySku()
        #end elif 
    #end removeSale()
            

    def reportmenu():
        #is the menu for when user chooses to access the inventory 
        #no returns 
        #no paramters 
        
        #option stores a string, the user's input 
        option = str(input('What would you like to do?\n1.Get reports\n2.Search by SKU\n3.Search by name\n4.Add a quantity\n5.Add an Item\n6.Remove an item\n7.Modify an item\n8.Put an item on sale\n9.Remove sale\nEnter: '))
        #while loop validates the option 
        while option not in ['1','2','3','4','5','6','7','8','9']:
            #user enters option until it is valid 
            option = str(input('\nTry again. What would you like to do?\n1.Get reports\n2.Search by SKU\n3.Search by name\n4.Add a quantity\n5.Add an Item\n6.Remove an item\n7.Modify an item\n8.Put an item on sale\n9.Remove sale\nEnter: ')) 
            os.system('clear')

    

        #if the user chose 1 
        if option == '1':
            #getReport() method is called 
            Reports.getReport()
        #end if 

        #if the user chose 2 
        elif option == '2':
            #searchItem() method is called  
            Reports.searchBySku()
        #end elif 

        #if the user chose 3    
        elif option == '3':
            #searchByName() method is called 
            Reports.searchByName()
        #end elif 

        #if the user chose 4 
        elif option == '4':
            #addQuantity() method is called 
            Reports.addQuantity()
        #end elif 
        
        #if the user chose 5
        elif option == '5':
            #addItem() method is called 
            Reports.addItem()
        #end elif 
        
        #if the user chose 6
        elif option == '6':
            #removeItem() method is called  
            Reports.deleteItem()
        #end elif 

        #if the user chose 7 
        elif option == '7':
            #modifyItem() method is called 
            Reports.modify()
        #end elif 

        #if the user chose 8
        elif option == '8':
            #saleItem() method is called 
            Reports.putAnItemOnSale()
        #end elif 

        #if the user chose 9
        elif option == '9':
            #removeSale() method is called 
            Reports.removeSale()
        #end elif 
        
        return
    #end reportmenu()
            
    def exitAndPrint():
    #exits and prints out inventory file 
    #no paramters 
    #no returns 
        #outputFile stores a string of the name of the new file 
        outputFile = "inventory." + datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%d-%m-%y") +".txt"
        #opening a file called outputFile to write into 
        with open(outputFile, 'w') as f:
            #for loop iterates through the product list 
            for item in Reports.prodList:
                #writes item information line by line into the file 
                f.write(f'{item.sku},{item.name},{item.ctgy},{item.qty},{item.rqty},{float(item.currentPrice):.2f},{float(item.salePercent):.2f},{float(item.profit):.2f}\n')
            #end for
            #closes the file 
            f.close()

        return 
    #end exitAndPrint()
#Reports.addItem()