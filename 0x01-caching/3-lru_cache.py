#!/usr/bin/env python3
"""This module function inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Defines the LRUCache class"""

    def __init__(self):
        """Initializes the LRUCache instance"""
        super().__init__()
        self.order_used_keys = []

    def put(self, key, item):
        """Adds an item to the cache using LRU algorithm"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order_used_keys.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.order_used_keys.append(key)

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is not None and key in self.cache_data:
            self.order_used_keys.remove(key)
            self.order_used_keys.append(key)
            return self.cache_data[key]
        return None
