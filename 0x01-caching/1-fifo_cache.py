#!/usr/bin/env python3
"""Doc module"""
from base_caching import BaseCaching
"""Importing class doc"""


class FIFOCache(BaseCaching):
    """Class doc"""
    def __init__(self):
        """Doc init methods"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        length = len(self.cache_data)
        lenitem = BaseCaching.MAX_ITEMS
        if key is not None or item is not None:
            if key not in self.cache_data.keys() and length >= lenitem:
                keys = list(self.cache_data.keys())
                pop = keys.pop(0)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")
            self.cache_data[key] = item

    def get(self, key):
        """Get methods doc"""
        return self.cache_data.get(key, None)
