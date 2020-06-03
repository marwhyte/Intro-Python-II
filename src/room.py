# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description,  items=None):
        self.name = name
        self.description = description
        self.items = items
        if items is None:
            self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return f"\n{self.name}\n{self.description}\nItems\n{self.__itemString__()}"

    def addItems(self, items):
        self.items.extend(items)
        return self.items

    def addItem(self, item):
        self.items.append(item)
        return self.items

    def removeItem(self, name):
        item = None
        itemIndex = None
        for index, item in enumerate(self.items):
            if item.name.lower() == name:
                item = item
                itemIndex = index
                break
        if item:
            return self.items.pop(itemIndex)
        else:
            return False

    def __itemString__(self):
        return "\n".join(str(item) for item in self.items)
