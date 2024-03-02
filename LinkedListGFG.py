class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


# Driver Code
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)


def printlist(head):
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next


printlist(head)
