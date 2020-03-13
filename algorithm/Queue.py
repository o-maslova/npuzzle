import heapq


class MyItem:
    def __init__(self, priority, arr, previous):
        self.priority = priority
        self.arr = arr
        self.previous = previous
        if not previous:
            self.cost = 0
        else:
            self.cost = previous.cost + 1


class MyPriorityQueue:
    def __init__(self):
        self.list_items = []
        self.id = 0

    def push(self, state):
        new_item = (state.priority, self.id, state)
        heapq.heappush(self.list_items, new_item)
        self.id += 1

    def pop(self):
        item = heapq.heappop(self.list_items)
        return item[2]

    def is_empty(self):
        if not self.list_items:
            return True
        return False

    def index(self, arr):
        for t in self.list_items:
            if arr == t[2].arr:
                return t[2]
        return None

