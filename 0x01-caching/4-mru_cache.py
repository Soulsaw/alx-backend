#!/usr/bin/env python3
'''
This modele implement the caching replacement fifo
'''
from base_caching import BaseCaching
'''
BaseCaching: inherit from the base_cache file
'''


class MRUCache(BaseCaching):
    '''This class inherit from the BaseCaching and have:
    Args:
    self.cache_data: from the parent constructor
    methods:
    put - To put a new item on the cache
    get - To get an item with her key
    '''
    def __init__(self):
        '''
        Implement the super methods from the parent
        '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        '''
        This function add an item in the cache
        Args:
        key - The key of the new item
        item - The item to add
        '''
        length = len(self.cache_data)
        lenitem = BaseCaching.MAX_ITEMS
        if key is not None and item is not None:
            if key not in self.cache_data.keys() and length >= lenitem:
                pop = self.keys.pop()
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")
                self.keys.append(key)
                self.cache_data[key] = item
            elif key in self.cache_data.keys():
                idx = self.keys.index(key)
                self.keys.pop(idx)
                self.keys.append(key)
                self.cache_data[key] = item
            else:
                self.keys.append(key)
                self.cache_data[key] = item

    def get(self, key):
        '''
        This method return a giving key item
        '''
        return self.cache_data.get(key, None)
