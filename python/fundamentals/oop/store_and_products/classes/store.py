class store:
    def __init__(self, name, type=None):
        self.name = name
        self.product = []
        self.type = type

    def add_product(self, new_product):
        self.product.append(new_product)
        return self

    def sell_product(self, id):
        for product in self.product:
            if product.get_id() == id:
                self.product.remove(product)
        return self

    def inflation(self, percent_increase):
        for product in self.product:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.product:
            if (product.get_category() == category):
                product.update_price(percent_discount, False)
        return self
