# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:24:02 2020

@author: henry
"""
    

class CompleteBinaryTree():
    def __init__(self):
        self.tree = []
        self.root = None
    
    def add_node(self, value):
        
        if len(self.tree) == 0:
            self.tree.append(value)
            self.root = self.tree[0]
        else:
            self.tree.append(value)
    
    def child_node(self, i):
        if len(self.tree) < 2 * i + 1:
            print("This is a leaf node")
        elif len(self.tree) >= 2 * i + 1 and len(self.tree) < 2 * i + 2:
            print("left child is:", self.tree[2 * i + 1])
        else:
            print("left child is:", self.tree[2 * i + 1])
            print("right child is", self.tree[2 * i + 2])

class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  def parent_idx(self, idx):
    """take an index and return the index of its parent
       Note: at index 0 we have none, so our heap actually starts at index 1 
    """
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count
  
  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
    
    min = self.heap_list[1]
    self.heap_list[1] = self.heap_list[self.count] #last element in the heap gets moved to top
    self.count -= 1
    self.heap_list.pop() #remove last element in the heap
    self.heapify_down()
    return min

  def add(self, element):
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()


  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child < right_child:
        return self.left_child_idx(idx)
      else:
        return self.right_child_idx(idx)
    
  def heapify_up(self):
    idx = self.count #last element's index
    swap_count = 0
    while self.parent_idx(idx) > 0:
      if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
        swap_count += 1
        tmp = self.heap_list[self.parent_idx(idx)] #store the value for parent node, for later swapping
        self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
        self.heap_list[idx] = tmp
      idx = self.parent_idx(idx)

    element_count = len(self.heap_list)
    if element_count > 10000:
      print("Heap of {0} elements restored with {1} swaps"
            .format(element_count, swap_count))
      print("")    
      
  def heapify_down(self):
    idx = 1
    # starts at 1 because we swapped first and last elements
    swap_count = 1
    while self.child_present(idx):
      smaller_child_idx = self.get_smaller_child_idx(idx)
      if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
        swap_count += 1
        tmp = self.heap_list[smaller_child_idx]
        self.heap_list[smaller_child_idx] = self.heap_list[idx]
        self.heap_list[idx] = tmp
      idx = smaller_child_idx

    element_count = len(self.heap_list)
    if element_count >= 10000:
      print("Heap of {0} elements restored with {1} swaps"
            .format(element_count, swap_count))
      print("")  


my_tree = CompleteBinaryTree()
my_tree.add_node(2)
my_tree.add_node(5)
my_tree.add_node(7)
my_tree.child_node(0)
  