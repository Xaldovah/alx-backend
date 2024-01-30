#!/usr/bin/env python3
"""This module function inherits from the BaseCaching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Defines the BasicCache class"""

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        return None
