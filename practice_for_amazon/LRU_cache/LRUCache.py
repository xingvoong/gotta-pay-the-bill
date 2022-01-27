'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity): Initialize the LRU cache with positive size capacity
- int get(int key) Return the value of the key if the key exists, otherwise return -1
- void put(int key, int value) Update the value of the key if the key exists.  Otherwise add the key-value pair to the cache.  If the number of keys exceeds the capacity from this operation evict the least recently used key

The functions pet and put must each run in O(1) average time complexity


- Solve this using a double linked list first,
- and then solve this using a order-linked list


Solve using double linked list:
+ head pointer:
  - add to front
  - get the front

+ tail pointer:
  - remove tail

- implement a double linked list in python first
'''
class Node:
  def __init__ (self, next = None, prev = None, val_array = None):
    self.next = next
    self.prev = prev
    self.val_array = val_array

class DDL:
  # always start with one node
  def __init__(self):
    self.head = None
    self.tail = None

  def print_it(self):
    ptr = self.head
    if (self.head == None):
      print("The list is empty")
      return
    print("The nodes in the doubly linked list are :")
    while ptr != None:
      print(ptr.val_array)
      ptr = ptr.next

  def add_to_front(self, val_array):
    new_node = Node(val_array = val_array)

    new_node.next = self.head
    new_node.prev = None

    if self.head:
      self.head.prev = new_node
    if not self.tail:
      self.tail = new_node

    self.head = new_node

  def remove_back(self):
    # if there is something to remove
    if self.tail.prev:
      self.tail = self.tail.prev
      self.tail.next = None
    else:
      self.head = None



class LRUCache:

  # init size
  # create node with capacity
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.size = 0
    self.head = DDL()

  def print_cache(self):

    if (self.head.head == None):
      print("The cache is empty")
      return
    ptr = self.head.head

    print("the cache is: ")
    while ptr != None:
      print(ptr.val_array)
      ptr = ptr.next


  def get(self, key: int):
    # put this key to the front
    ptr = self.head.head
    while ptr:
      if ptr.val_array[0] == key:
        print("key to get exist")
        print(ptr.val_array[0])

        # move it to the front
        self.head.add_to_front([key, ptr.val_array[0]])
        self.size +=  1
        if self.size > self.capacity:
          self.head.remove_back()
          self.size -= 1

        return ptr.val_array[1]
      ptr = ptr.next

    print("no key")
    return -1

  def put(self, key: int, value: int):
    # check if this key already in the cache
    ptr = self.head.head

    self.head.add_to_front([key, value])
    self.size += 1
    if self.size > self.capacity:
      self.head.remove_back()
      self.size -= 1


# Code execution
if __name__ == '__main__':
  # head = DDL()
  # head.add_to_front([3, 3])
  # head.add_to_front([2, 2])
  # head.add_to_front([1, 1])

  # head.print_it()

  cache_instance = LRUCache(2)
  cache_instance.print_cache()
  cache_instance.put(1, 1)
  cache_instance.put(2, 2)
  cache_instance.print_cache()
  cache_instance.get(1)
  cache_instance.print_cache()
  cache_instance.put(3, 3)
  cache_instance.print_cache()
  cache_instance.get(2)
  cache_instance.put(4, 4)
  cache_instance.get(1)
  cache_instance.get(3)
  cache_instance.get(4)

