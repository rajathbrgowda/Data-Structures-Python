class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubleLikedList:
    def __init__(self):
        self.head

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Double Linked List is Empty")
            return
        itr = self.head
        dlltr = ''

        while dlltr:
            dlltr += str(itr.data) + "--->"
            itr = itr.next
        print(dlltr)

if __name__ == '__main__':
    ll = doubleLikedList()