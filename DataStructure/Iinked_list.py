# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
  
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node
    
# Our LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
  
    def get_head_node(self):
        return self.head_node
  
# Add your insert_beginning and stringify_list methods below:
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def insert_middle(self, new_value, position):
        assert position > 0, "use insert_beginning method"
        new_node = Node(new_value)
        index_position = 0
        previous_node = self.head_node
        
        while index_position + 1 != position:
            previous_node = previous_node.get_next_node()
            index_position = index_position + 1
            
        temp_node = previous_node.get_next_node()
        new_node.set_next_node(temp_node)
        previous_node.set_next_node(new_node)
    
    def remove_node(self, value_to_remove):
        record = []
        current_node = self.head_node
        if current_node.value == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node.get_next_node() != None:
                temporary_node = current_node.get_next_node()
                if temporary_node.get_value() == value_to_remove:
                    current_node.set_next_node(temporary_node.get_next_node())
                    record.append(temporary_node.get_value())
                else:
                    current_node = temporary_node   
        if len(record) == 0:
            print("value not found in the list")
    
        
        
    def reverse_list(self):
        if self.head_node.get_next_node() == None:
            return self.stringify_list()
        else:
            temp_node1 = self.head_node
            next_node1 = temp_node1.get_next_node()
            while next_node1.get_next_node() != None:
                temp_node2 = next_node1.get_next_node()
                next_node1.set_next_node(temp_node1)
                temp_node1 = next_node1
                next_node1 = temp_node2
            
            next_node1.set_next_node(temp_node1)
            self.head_node.set_next_node(None)
            self.head_node = next_node1
            
    
    def stringify_list(self):
        temp = self.head_node
        while temp.get_next_node() != None:
            print(str(temp.get_value()), end = ">-")
            temp = temp.get_next_node()
        print(str(temp.get_value()))
    
    def find_max(self):
        temp_node = self.head_node
        result = temp_node.get_value()
        while temp_node.get_next_node() != None:
            temp_node = temp_node.get_next_node()
            if result < temp_node.get_value():
                result = temp_node.get_value()
        return result
    


# =============================================================================
# test_list = LinkedList(5)
# test_list.insert_beginning(6)
# test_list.insert_beginning(70)
# test_list.insert_beginning(70)
# test_list.insert_beginning(5675)
# test_list.insert_beginning(90)
# test_list.insert_middle(42, 2)
# print(test_list.find_max())  
# test_list.remove_node(5)
# test_list.stringify_list()
# =============================================================================
# =============================================================================
# test_list.reverse_list()
# test_list.stringify_list()
# =============================================================================

