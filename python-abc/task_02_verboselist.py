#!/usr/bin/env python3

class VerboseList(list):
    """
    A subclass of list that prints messages whenever an element is added, 
    removed, or modified.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a message.
        
        :param item: The item to be added to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, items):
        """
        Extend the list with multiple items and print a message.
        
        :param items: An iterable containing items to add to the list.
        """
        super().extend(items)
        number_of_items = len(items)
        print(f"Extended the list with [{number_of_items}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and print a message.
        
        :param item: The item to remove from the list.
        """
        super().remove(item) 
        print(f"Removed [{item}] from the list.") 

    def pop(self, index=-1):
        """
        Remove and return an item at the given index (default: last item) 
        and print a message.
        
        :param index: The index of the item to remove (default is -1, meaning the last item).
        :return: The item that was removed.
        """
        item = super().pop(index)  
        print(f"Popped [{item}] from the list.")
        return item  
