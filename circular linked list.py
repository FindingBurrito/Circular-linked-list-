


# Program 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.size += 1

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1

    def remove_from_head(self):
        if self.head is None:
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        temp.next = None
        return temp.data

    def remove_from_tail(self):
        if self.head is None:
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = self.head
        self.size -= 1
        temp.next = None
        return temp.data

    def display(self):
        if self.head is None:
            print("Here is the list : List is empty")
            return
        temp = self.head
        print("Here is the list :", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

def main():
    CLL = CircularLinkedList()

    CLL.insert_at_tail(10)
    CLL.insert_at_tail(20)
    CLL.display()

    CLL.insert_at_tail(30)
    CLL.display()

    CLL.insert_at_head(5)
    CLL.display()

    CLL.insert_at_head(1)
    CLL.display()

    print(f"Remove {CLL.remove_from_head()} from head of the list")
    CLL.display()

    print(f"Remove {CLL.remove_from_head()} from head of the list")
    CLL.display()

    print(f"Remove {CLL.remove_from_tail()} from tail of the list")
    CLL.display()

    print(f"Remove {CLL.remove_from_tail()} from tail of the list")
    CLL.display()

    print(f"Remove {CLL.remove_from_tail()} from tail of the list")
    CLL.display()

if __name__ == "__main__":
    main()
