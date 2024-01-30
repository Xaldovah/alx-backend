#!/usr/bin/env python3
"""This mod func inherits from base_caching and is a caching system"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Defines the MRUCache class"""

    def __init__(self):
        """Initializes the MRUCache instance"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Adds an item to the cache using MRU algorithm"""
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.usage_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return item
