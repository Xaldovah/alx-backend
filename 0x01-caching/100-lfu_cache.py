#!/usr/bin/env python3
"""This module function inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Defines the LFUCache class"""

    def __init__(self):
        """Initializes the LFUCache instance"""
        super().__init__()
        self.frequency_count = {}

    def put(self, key, item):
        """Adds an item to the cache using LFU algorithm"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_frequency = min(self.frequency_count.values())
                least_frequent_keys = [k for k, v in self.frequency_count.items() if v == min_frequency]
                if len(least_frequent_keys) > 1:
                    discarded_key = min(self.cache_data, key=lambda k: self.cache_data[k][1])
                else:
                    discarded_key = least_frequent_keys[0]
                del self.cache_data[discarded_key]
                del self.frequency_count[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item, 0
            self.frequency_count[key] = 0

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is not None and key in self.cache_data:
            self.frequency_count[key] += 1
            return self.cache_data[key][0]
        return None
