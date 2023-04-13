


class Node;

def __init__(self, date);

self.date = date
self.next = None


class stack:

    def __init__(self);
    self.top = None
    self.size = 0

    def push(self,elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.size += 1