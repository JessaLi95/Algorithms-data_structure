class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoulelyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -= 1            
        return temp

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index <= self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1 - index):
                temp = temp.prev
        return temp




myDoubleList = DoulelyLinkedList(1)
myDoubleList.append(2)
myDoubleList.prepend(0)
myDoubleList.append(3)
myDoubleList.append(4)
myDoubleList.append(5)
myDoubleList.print_list()
print(myDoubleList.get(0).value)
print(myDoubleList.get(1).value)
print(myDoubleList.get(2).value)
print(myDoubleList.get(3).value)
print(myDoubleList.get(4).value)