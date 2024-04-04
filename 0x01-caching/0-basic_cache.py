#!/usr/bin/env python3
'''
This is the documentation of the module
'''
from base_caching import BaseCaching
'''The import is well documented here'''


class BasicCache(BaseCaching):
    '''
    This class inherit from the BaseCaching class
    '''
    def put(self, key, item):
        '''
        add an item with his key
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        retrieve an existing values of a key or None
        '''
        return self.cache_data.get(key, None)
