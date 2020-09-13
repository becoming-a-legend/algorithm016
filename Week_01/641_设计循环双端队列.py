class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = []
        self.num = k
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) < self.num:
            self.deque.insert(0, value)
            return True
        else:
            return False


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) < self.num:
            self.deque.append(value)
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.deque:
            del self.deque[0]
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.deque:
            self.deque.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.deque:
            return self.deque[0]
        else:
            return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.deque:
            return self.deque[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.deque:
            return False
        else:
            return True
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.deque) == self.num:
            return True
        else:
            return False
        