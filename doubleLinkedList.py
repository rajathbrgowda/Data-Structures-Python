class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubleLikedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head,None)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None,itr)

    def print_forward(self):
        if self.head is None:
            print("Double Linked List is Empty")
            return
        itr = self.head
        dlltr = ''
        while itr:
            dlltr += str(itr.data) + '--->'
            itr = itr.next
        print(dlltr)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count += 1
            itr=itr.next
        return count

    def print_backward(self):
        if self.head is None:
            print("Double Linked List is Empty")
            return
        itr = self.head
        dlltr = ''
        while itr:
            if itr.next is None:
                new_itr = itr
                while new_itr:
                    dlltr += str(new_itr.data) + '--->'
                    new_itr = new_itr.prev
            itr = itr.next
        print(dlltr)

    def insert_values(self,data):
        self.head = None
        for i in data:
            self.insert_at_end(i)

if __name__ == '__main__':
    ll = doubleLikedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()