#!/usr/bin/env python3
"""Doc module"""
BaseCaching = __import__('base_caching').BaseCaching
"""Importing class doc"""


class BasicCache(BaseCaching):
    """Class doc"""
    def __init__(self):
        """Doc init methods"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get methods doc"""
        if key is not None or key in self.cache_data.keys():
            return self.cache_data.get(key)
        else:
            return None
