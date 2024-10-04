class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def talk(self):
        if self.conversation is not None:
            return f"[{self.name} says]: {self.conversation}"
        else:
            return None

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            return True
        else:
            return False

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gift = None

    def set_gift(self, gift):
        self.gift = gift
