#!/usr/bin/env python3
'''
This modele implement the caching replacement fifo
'''
from base_caching import BaseCaching
'''
BaseCaching: inherit from the base_cache file
'''


class LIFOCache(BaseCaching):
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

    def put(self, key, item):
        '''
        This function add an item in the cache
        Args:
        key - The key of the new item
        item - The item to add
        '''
        length = len(self.cache_data)
        lenitem = BaseCaching.MAX_ITEMS
        if key is not None or item is not None:
            if key not in self.cache_data.keys() and length >= lenitem:
                last = self.cache_data.popitem()
                print(f"DISCARD: {last[0]}")
            self.cache_data[key] = item

    def get(self, key):
        '''
        This method return a giving key item
        '''
        return self.cache_data.get(key, None)
