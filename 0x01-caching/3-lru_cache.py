#!/usr/bin/env python3
"""Doc module"""
BaseCaching = __import__('base_caching').BaseCaching
"""Import class doc"""


class LRUCache(BaseCaching):
    """Class doc"""
    def __init__(self):
        """Doc init methods"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        length = len(self.cache_data)
        lenitem = BaseCaching.MAX_ITEMS
        if key is not None or item is not None:
            if key not in self.cache_data.keys() and length >= lenitem:
                pop = self.keys.pop(0)
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
        """Get methods doc"""
        if key is not None or key in self.cache_data.keys():
            return self.cache_data.get(key)
        else:
            return None
