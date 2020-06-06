# -*- coding: utf-8 -*-
"""
Created on Tue May  5 07:54:14 2020

@author: kakuitsuhi
"""

from Iinked_list import Node

class Stack():
    def __init__(self, value = None):
        self.head_node = Node(value)
    
    def push(self, new_value):
        new_node = Node(new_value)
        print("Insert " + str(new_value) + " to the stack")
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def pop_head(self):
        if self.head_node.value == None:
            return "Stack is empty"
        result = self.head_node
        self.head_node = self.head_node.get_next_node()
        return result.value
    
    def peek(self):
        return self.head_node.get_value()
    
    def is_empty(self):
        if self.head_node.get_value() == None:
            return True
        return False

class Queue():
    def __init__(self, max_size = None):
        self.head_node = None
        self.tail = None
        self.size = 0
        self.max_size = max_size
    
    def has_space(self):
        if self.max_size == None:
            return True
        return self.size < self.max_size
    
    def is_empty(self):
       return self.size == 0
   
    def peek(self):
        if self.size > 0:
            print(self.head_node.get_value())
        print("Queue is empty")
        
    def enqueue(self, value):
        entry_to_add = Node(value)
        if self.has_space():
            if self.size == 0:
                self.head_node = entry_to_add
                self.tail = entry_to_add
                
            else:
                
                self.tail.set_next_node(entry_to_add)
                self.tail = entry_to_add
            
            self.size = self.size + 1
        else:
            print("Queue is full! Cannot add more elements")
    
    def dequeue(self):
        if self.is_empty():
            print("empty queue, no entry to delete")
            
        else:
            remove = self.head_node
            if self.size == 1:
                
                self.head_node = None
                self.tail = None
                
            else:
                temp_node = self.head_node.get_next_node()
                self.head_node = temp_node
            self.size = self.size - 1
            return remove.get_value
            

        
        
   

# =============================================================================
# test_stack = Stack()
# test_stack.push(2)
# test_stack.push(3)
# print(test_stack.peek())
# print(test_stack.head_node.value)
# print(test_stack.head_node.get_next_node().value)
# print(test_stack.pop_head())
# print(test_stack.pop_head())
# print(test_stack.pop_head())   
# print(test_stack.is_empty())     
# =============================================================================
my_q = Queue()
my_q.enqueue(5)
my_q.enqueue(7)
my_q.peek() 
my_q.dequeue()
my_q.peek()     
my_q.dequeue()
my_q.peek()  