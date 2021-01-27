'''
1. medium, array, hashtable, list, design.

2. problem statement:

Implement the RandomizedSet class:
+ bool insert(int val) Inserts an item val into the set if not present.
Returns true if the item was not present, false otherwise.
+ bool remove(int val) Removes an item val from the set if present.
Returns true if the item was present, false otherwise.
+ int getRandom() Returns a random element from the current set of elements
(it's guaranteed that at least one element exists when this method is called).
Each element must have the same probability of being returned.
Requirements: each function works in average O(1) time?

3. solution in plain English/ pseudocode
Intuition:
to achieve constant time for insert and remove,
a dictionary would do the job
but it can not get a random element in O(1) time
Therefor a list is needed.
For a list:
insert and remove to the end or the beginning of a list
are O(1) time.
Implementation:
init:
list: a list of values
dict: key/value pair is value and it's index in the list
insert:
to dict: key/value = value/index, add to the end of the list
to list: append to the end of the list
remove:
+ always remove from the end of the list:
    + swap the value need to remove to the end of the list
    + swap the value at the end of the list to the position of
        the value that need to remove
    + remove value from the list
    + update the swap value position in dict
    + remove value from the dict
getRandom:
 choice function in python

4: implementation

'''


class RandomizedSet(object):
    def __init__(self):

        self.dict = {}
        self.list = []

    def insert(self, val):
        """
            Inserts a value to the set.
            Returns true if the set did not
            already contain the specified element.
            :type val: int
            :rtype: bool
        """
        if val not in self.list:
            self.list.append(val)
            self.dict[val] = len(self.list)
            return True
        return False

    def remove(self, val):
        """
            Removes a value from the set.
            Returns true if the set contained the specified element.
            :type val: int
            :rtype: bool
        """

        if val in self.list:
            last_element = self.list[-1]
            val_index = self.dict[val]
            self.list[-1] = val
            self.list[val_index] = last_element
            self.dict[last_element] = val_index

            self.list.pop()
            del self.dict[val]

            return True
        return False

    def getRandom(self):
        """
            Get a random element from the set.
            :rtype: int
        """
        from random import choice
        return choice(self.list)


randomizedSet = RandomizedSet()
assert randomizedSet.insert(1) is True
assert randomizedSet.remove(2) is False
assert randomizedSet.insert(2) is True
assert randomizedSet.insert(3) is True
assert randomizedSet.insert(4) is True
print(randomizedSet.getRandom())
