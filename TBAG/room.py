class Room:
    def __init__(self, room_name: str):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.locked = False

    def set_description(self, room_description: str):
        self.description = room_description

    def describe(self):
        print(self.description)

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def link_room(self, room_to_link, direction: str):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(f"You are in the {self.name}")
        print("--------------------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")
        if self.item is not None:
            print(f"You see a {self.item.get_name()} here.")

    def move(self, direction: str):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self

    def get_name(self):
        return self.name
