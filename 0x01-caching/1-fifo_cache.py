#!/usr/bin/env python3
"""Doc module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """Doc init methods"""
        super().__init__()

    """Class doc"""
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
        if key is not None or key in self.cache_data.keys():
            return self.cache_data.get(key)
        else:
            return None
