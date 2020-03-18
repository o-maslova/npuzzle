class MyItem:
    def __init__(self, priority, cost, arr):
        self.priority = priority
        self.arr = arr
        self.cost = cost


class MyQueue:
    def __init__(self):
        self.list_items = {}

    def append(self, item):
        list_to_insert = self.list_items.get(item.priority)
        if list_to_insert:
            self.list_items[item.priority].append(item)
        else:
            self.list_items[item.priority] = [item]

