class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        newNode = Node(data)
        newNode.next_node = self.head
        self.head = newNode

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        print(self.size())
        if index < 0:
            return "you can't insert at this index"
        if index > self.size():
            return "you can't insert at this index"

        if index == 0:
            self.add(data)
            return

        if index > 0:
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev = current
            next = current.next_node
            prev.next_node = new_node
            new_node.next_node = next

    def remove(self, key):
        current = self.head
        prev = None
        found = False
        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
                current.next_node = None
                return True
            else:
                prev = current
                current = current.next_node

            print(f"prev: {prev}")
            print(f"curent: {current}")
        return current
        # prev = current
        # next = current.next_node

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(f"{current.data}")
            current = current.next_node
        return " -> ".join(nodes)


l = LinkedList()
# print(l.size())
l.add(4)
# l.add(3)
l.add(2)
l.add(1)
# print(l.size())
# print(l)


l.insert(3, 2)
l.insert(5, 4)
l.insert(6, 5)
l.remove(1)

print(l)
l.insert(3, 2)

print(l)
print(l.size())

# res =l.is_empty()
# print(res)

# res2 = l.search(5)

# print(res2)
