class MyItem:
    def __init__(self, priority, arr):
        self.priority = priority
        self.arr = arr


class MyQueue:
    def __init__(self):
        self.list_items = []

    def append(self, item):
        # f = open("guru99.txt", "a+")
        if len(self.list_items) == 0:
            self.list_items.append(item)
        else:
            i = -1
            # f.write('new line\n\n')
            for child in self.list_items:
                # f.write('child: ' + str(child.priority) + '\t-\t' + 'item: ' + str(item.priority) + '\n')
                if child.priority >= item.priority:
                    i = self.list_items.index(child)
                    self.list_items.insert(i, item)
                    # f.write(str(i) + '\t-\t' + (''.join(str(e) for e in item.arr) + '\n'))
                    break
            if i == -1:
                self.list_items.append(item)

