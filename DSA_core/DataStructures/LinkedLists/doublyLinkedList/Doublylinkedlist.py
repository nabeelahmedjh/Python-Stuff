class Node:
    def __init__(self, value=0, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DLL:
    def __init__(self) -> None:
        self.head = None

    def insert_first(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_last(self, value):
        node = Node(value)
        last = self.head
        if self.head is None:
            self.insert_first(value)
            return
        while last.next:
            last = last.next

        node.prev = last
        last.next = node

    def display(self):
        node = self.head
        last = self.head

        while node:
            if node.next is None:
                last = node
            print(node.value, end="-->")
            node = node.next
        print("End")

        print("Printing in reverse order")

        while last:
            print(last.value, end="-->")
            last = last.prev
        print("START")


def main():
    l = DLL()
    l.insert_last(1)
    l.insert_first(2)
    l.insert_first(3)
    l.insert_first(4)
    l.insert_last(3)
    l.display()


if __name__ == "__main__":
    main()
