from tkinter.messagebox import NO


class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


class LL:
    def __init__(self, Node=None) -> None:
        self.head = Node

    def add_first(self, value):
        node = Node(value, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head
        while itr:
            print(str(itr.value), end="--->")
            itr = itr.next

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(value=value)

    def remove_item(self, value, position=None):

        if self.head.value == value:
            self.head = self.head.next

        pointer = Node(self.head)
        curr = self.head.next

        while curr:
            nxt = curr.next
            if curr.value == value:
                pointer.next = nxt
            else:
                pointer = curr
            curr = nxt

    # Big TODO
    # def reverse(self):
    #     itr = self.head
    #     next_head = itr.next
    #     while itr:
    #         if
    #         head = next_head
    #         next_head = head.next
    #         head.next = itr
    #         itr = head


def main():

    l = LL()
    l.append(7)
    l.add_first(12)
    l.append(10)
    l.add_first(34)
    l.remove_item(10)
    l.append(1)
    l.append(45)
    l.reverse()
    l.print()


if __name__ == "__main__":
    main()
