""" The python program mimics a real world grocery list"""
# GroceryList class


class GroceryList:
    """Initialising the class attributes"""

    def __init__(self):
        self.numberOfItems = 0  # counts the items of the list
        self.items = []  # Holds the items of our list
        self.position = -1  # Keeps track of each items position

    """Adding items to our list"""
    def insert_item(self, item):
        self.items.append(item)
        self.numberOfItems += 1
        self.position += 1

    """Removing item from our list"""
    def remove_item(self):
        if self.position == -1:
            print("The List is Empty!")
        else:
            self.items.pop(self.position)
            self.numberOfItems -= 1
            self.position -= 1

    """Formatted display of our list"""
    def print_list(self):
        print("<-- Your Grocery List -->")
        for item in self.items:
            print(f"> {item}")

    """Return number of items"""
    def number_of_items(self):
        return self.numberOfItems


myList = GroceryList()
myList.insert_item("beans")
myList.insert_item("corn")
myList.insert_item("yams")
myList.print_list()
myList.remove_item()
myList.print_list()
print(myList.number_of_items())
