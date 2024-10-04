class Item:
    def __init__(self):
        self.name = None

    def set_name(self, item_name: str):
        self.name = item_name

    def get_name(self):
        return self.name

class Key(Item):
    def __init__(self):
        super().__init__()
        self.name = "rusty key"

class Sword(Item):
    def __init__(self):
        super().__init__()
        self.name = "sword"
