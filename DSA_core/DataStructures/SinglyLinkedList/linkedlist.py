from tkinter.messagebox import NO


class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


class LL:
    def __init__(self, Node=None) -> None:
        self.head = Node
        self.tail = Node
        self.len = 0
        if Node is not None:
            self.len += 1

    def add_first(self, value):
        node = Node(value, self.head)
        self.head = node
        self.len += 1
        if self.tail is None:
            self.tail = self.head

    def add_last(self, value):

        if self.tail is None:
            self.add_first(value)
            return

        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.len += 1

    def add_at(self, value, index):
        if index > self.len or index < 0:
            raise IndexError

        if index == 0:
            self.add_first(value)
            return
        if index == self.len:
            self.add_last(value)
            return

        pos = 0
        itr = self.head

        while itr.next:

            if pos == index - 1:
                n = Node(value, next=itr.next)
                itr.next = n
                break

            itr = itr.next
            pos += 1

        self.len += 1

    def remove_first(self):
        self.head = self.head.next
        self.len -= 1

        if self.head is None:
            self.tail = None

    def remove_last(self):
        curr = self.head
        prev = Node(next=self.head)

        while curr:

            if curr.next == self.tail:
                self.tail = curr
                self.tail.next = None
                self.len -= 1
                return
            curr = curr.next

    def remove_index(self, index):
        if index == 0:
            self.remove_first()
            return

        if index == self.len - 1:
            self.remove_last()
            return

        itr = self.head.next
        pos = 1
        while itr:
            nxt = itr.next
            if pos == index - 1:
                itr.next = nxt.next
                self.len -= 1
                return
            pos += 1
            itr = nxt

    def print(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head
        while itr:
            print(str(itr.value), end="--->")
            itr = itr.next
        print("End")
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
    l.add_last(7)
    l.add_first(12)
    l.add_last(10)
    l.add_first(34)
    l.add_last(1)
    l.add_last(45)
    l.add_at(99, 0)
    l.add_at(1, 0)
    l.add_at(9999, 3)
    l.remove_first()
    l.remove_last()
    l.remove_index(3)
    l.print()
    print(l.len)


if __name__ == "__main__":
    main()
