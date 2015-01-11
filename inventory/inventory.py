import product

class Inventory:

    def __init__(self):
        self.product_list = []

    def add_product(self, pid):
        self.product_list.append(pid)
    
    def remove_product(self, pid):
        if pid in product_list:
            self.product_list.remove(pid)
    
    def display_inventory(self):
        print self.product_list

if __name__ == "__main__":
    inventory = Inventory()
    toy = product.Product(1,"Ball", 1,2,3)
    inventory.add_product()
    inventory.display_inventory()
