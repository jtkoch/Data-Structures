"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# Array
# class Stack:
#     def __init__(self, storage=[]):
#         self.size = 0
#         self.storage = storage

#     def __str__(self):
#         return f'{self.storage}'

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop()



# Re-implemented the stack class with linked list
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        current_node = self.storage.head 
        length = 0

        while current_node:
            length += 1
            current_node = current_node.next_node
        return length    

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        return self.storage.remove_head()





# Linked List 
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None        

    def add_to_head(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None

        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None    
            return head_value

        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head     

        while current_node is not None:
            if current_node.value == value:
                return True

            current_node = current_node.next_node
        return False
    
    def get_max(self):
        if self.head is None:
            return

        current_node = self.head
        max_value = 0
        while current_node is not None:
            if current_node.value > max_value:
                print('current',current_node.value)
                max_value = current_node.value
                print('max', max_value)
            current_node = current_node.next_node
        return max_value