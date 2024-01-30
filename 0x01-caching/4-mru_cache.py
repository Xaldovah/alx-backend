#!/usr/bin/env python3
"""This mod func inherits from base_caching and is a caching system"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Defines the MRUCache class"""

    def __init__(self):
        """Initializes the MRUCache instance"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache using MRU algorithm"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = max(self.cache_data, key=lambda k: self.cache_data[k])
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
