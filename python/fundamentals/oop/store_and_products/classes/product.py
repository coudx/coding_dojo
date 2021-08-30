class product:
    def __init__(self, name=None, category=None, price=0, id=None):
        self.name = name
        self.price = price
        self.category = category
        self.id = id

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= 1 + percent_change/100
        else:
            self.price *= 1 - percent_change/100

    def print_info(self):
        print("Product Name: {}   Category: {}  Price: {}".format(
            self.name, self.category, self.price))

    def get_category(self):
        return self.category

    def get_id(self):
        return self.id
