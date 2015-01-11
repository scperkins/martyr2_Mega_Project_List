#import inventory
class Product:
    def __init__(self, pid, name, price, qty, weight):
        self.pid = pid
	self.name = name
	self.price = price
	self.qty = qty
	self.weight = weight
	
    def update_price(self, new_price):
	if new_price < 0:
            print "The price cannot be a negative value!"			
	else:
	    self.price = new_price		
    def update_qty(self, new_qty):
	#TODO This
	self.qty += inventory
    def update_weight(self, new_weight):
        self.weight = new_weight

if __name__ == "__main__":
    toy = Product(1, "Ball", 2.0, 1, 2)
    print "pid:", toy.pid
    print "name:", toy.name
    print "price:", toy.price
    print "qty:", toy.qty
    print "weight:", toy.weight

    toy.update_price(-10.50)
    print toy.price
