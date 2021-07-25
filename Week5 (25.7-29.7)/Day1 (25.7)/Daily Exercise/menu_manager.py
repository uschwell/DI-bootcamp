from _typeshed import Self


class MenuManager():
    def __init__(self):
        self.menu={
            price:'',
            spice:'',
            gluten: False,
        }

    def add_item(self, name, price, spice, gluten):
        self.menu[name]=name