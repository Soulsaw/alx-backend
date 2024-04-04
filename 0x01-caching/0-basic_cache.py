#!/usr/bin/env python3
"""Doc module"""
from base_caching import BaseCaching
"""Import doc"""


class BasicCache(BaseCaching):
    """Class doc"""
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get methods doc"""
        return self.cache_data.get(key, None)
