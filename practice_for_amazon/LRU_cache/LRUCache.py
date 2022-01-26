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
class LRUCache:

  def __init__(self, capacity: int):


  def get(self, key: int):


  def put(self, key: int, value: int):