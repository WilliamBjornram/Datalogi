class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None   
        self.__size = 0

    def isEmpty(self):
        if self.__first == None:
            return True
        else:
            return False

    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.__last = self.__first = new_node
        else:
            self.__last.next = new_node
            self.__last = new_node
        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        
        elif self.__size == 1:
            temp = self.__first
            self.__first = None
            self.__last = None
            self.__size -= 1
            return temp
        else:
            temp = self.__first
            self.__first = self.__first.next
            self.__size -= 1
            return temp

    def size(self):
        return self.__size

    
    def display(self):
        current = self.__first
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    


if __name__ == "__main__":
    linked_queue = LinkedQ()
    linked_queue.enqueue(10)
    linked_queue.enqueue(20)
    linked_queue.enqueue(30)
    print("Current size:", linked_queue.size())
    item1 = linked_queue.dequeue()
    item2 = linked_queue.dequeue()
    print("Dequeued items:", item1, item2)
    print("Current size:", linked_queue.size())