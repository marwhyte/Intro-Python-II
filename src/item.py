class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} - is a {self.description}"

    def pickUp(self):
        print(f"picked up a {self.name}")

    def drop(self):
        print(f"dropped a {self.name}")
