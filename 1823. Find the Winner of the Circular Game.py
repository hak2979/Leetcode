class Solution:
    class Node:
        def __init__(self, value: int):
            self.value = value
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = self.tail = None

        def insert(self, value: int):
            tempNode = Solution.Node(value)
            if self.head is None:
                self.head = self.tail = tempNode
                self.tail.next = self.head
            elif self.head == self.tail:
                self.tail = tempNode
                self.head.next = self.tail
                self.tail.next = self.head
            else:
                self.tail.next = tempNode
                self.tail = tempNode
                self.tail.next = self.head

        def delete(self, current: int, index: int):
            index -= 1

            temp_ = self.head
            while temp_.value != current:
                temp_ = temp_.next

            if self.head is None:
                print("The list is empty.")
                return

            current = temp_
            previous = None
            for _ in range(index):
                previous = current
                current = current.next
            
            if current==self.head:
                self.head=self.head.next
                return self.head.value

            # Deleting a middle or tail node
            if current == self.tail:
                self.tail = previous
                self.tail.next = self.head
            else:
                previous.next = current.next

            return current.next.value if current != self.tail else self.head.value

        def length_1(self) -> bool:
            return self.head == self.tail

        def value_(self) -> int:
            return self.head.value

        def disp(self):
            if self.head is None:
                return
            temp = self.head
            while True:
                print(temp.value, "->", end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            
            print("------")

    def findTheWinner(self, n: int, k: int) -> int:
        list_=[]
        for i in range(n):
            list_.append(i+1)
        
        k-=1

        while len(list_)>1:
            for j in range(k):
                temp=list_.pop(0)

                list_.append(temp)
            
            list_.pop(0)
      

        return list_[0]

        
