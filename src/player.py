# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom, inventory=[]):
        self.currentRoom = currentRoom
        self.name = name
        self.inventory = inventory

    def __addItem__(self, item):
        self.inventory.append(item)
        item.pickUp()
        return self.inventory

    def __removeItem__(self, index):
        item = self.inventory.pop(index)
        item.drop()
        return self.inventory

    def pickupItem(self, name):
        item = self.currentRoom.removeItem(name)
        if item:
            return self.__addItem__(item)
        else:
            return False

    def dropItem(self, name):
        item = None
        itemIndex = None
        for index, item in enumerate(self.inventory):
            if item.name.lower() == name:
                item = item
                itemIndex = index
                break
        if item:
            self.currentRoom.addItem(item)
            return self.__removeItem__(itemIndex)
        else:
            return False

    def inventoryString(self):
        return "\n".join(str(item) for item in self.inventory)
