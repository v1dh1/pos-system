class Product:
#class stores information about a product 

    def __init__(self, sku, name, ctgy, qty, rqty, vendorPrice, markUpPercent, regPrice, salePercent, currentPrice):     
        #initalises the attributes 
        #no returns 
        #no parameters 
        self.sku = sku
        self.name = name
        self.ctgy = ctgy
        self.qty = int(qty)
        self.rqty = int(rqty)
        self.vendorPrice = float(vendorPrice)
        self.markUpPercent = float(markUpPercent)
        self.regPrice = float(regPrice)
        self.salePercent = float(salePercent)
        self.currentPrice = float(currentPrice)
        self.profit = self.currentPrice - self.vendorPrice
        if self.qty < self.rqty:
            self.warning = True
        else:
            self.warning = False
    #end __init__
#end Product 