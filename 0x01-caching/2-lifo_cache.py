#!/usr/bin/env python3
"""This module function iherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Defines the LIFOCache class"""

    def __init__(self):
        """Initializes the LIFOCache instance"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache using LIFO algo"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        return None
