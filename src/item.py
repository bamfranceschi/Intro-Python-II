class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f"{self.name}, {self.desc}"

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")
