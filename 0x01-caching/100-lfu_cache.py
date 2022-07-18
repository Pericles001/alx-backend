#!/usr/bin/python3
""" 5. LFU Caching
"""

from enum import Enum
from heapq import heappush, heappop
from itertools import count

BaseCaching = __import__("base_caching").BaseCaching


class HeapItemStatus(Enum):
    """ HeapItemStatus class.
    """
    ACTIVE = 1
    INACTIVE = 2


class LFUCache(BaseCaching):
    """ Create a class LFUCache that inherits from BaseCaching and is a caching
    system
    """

    def __init__(self):
        """ Init
        """
        super().__init__()
        self.heap = []
        self.map = {}
        self.counter = count()

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data the item value for
        the key key
        """
        if key and item:
            if key in self.cache_data:
                self.rehydrate(key)
            else:
                if self.is_full():
                    self.evict()
                self.add_to_heap(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.rehydrate(key)
            return self.cache_data.get(key)

    def is_full(self):
        """ If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """ you must print DISCARD: with the key discarded and following by a
        new line
        """
        while self.heap:
            _, __, item, status = heappop(self.heap)
            if status == HeapItemStatus.ACTIVE:
                print("DISCARD: " + str(item))
                del self.cache_data[item]
                return

    def rehydrate(self, key):
        """ Marks current item as inactive and reinserts updated count back
        into heap.
        """
        entry = self.map[key]
        entry[-1] = HeapItemStatus.INACTIVE
        self.add_to_heap(key, entry[0])

    def add_to_heap(self, key, count=0):
        """ Adds a new entry into heap.
        """
        entry = [1 + count, next(self.counter), key, HeapItemStatus.ACTIVE]
        self.map[key] = entry
        heappush(self.heap, entry)
