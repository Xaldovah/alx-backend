#!/usr/bin/env python3
"""This module function inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Defines the LFUCache class"""

    def __init__(self):
        """Initializes the LFUCache instance"""
        super().__init__()
        self.frequency_count = {}
        self.used_order = {}

    def put(self, key, item):
        """Adds an item to the cache using LFU algorithm"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self._update_frequency_and_order(key)
        else:
            self.frequency_count[key] = 1
            self.used_order[key] = 0

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self._find_discard_key()
            del self.cache_data[discarded_key]
            del self.frequency_count[discarded_key]
            del self.used_order[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]
        self._update_frequency_and_order(key)
        return item

    def _update_frequency_and_order(self, key):
        """Updates frequency and usage order of a key"""
        self.frequency_count[key] += 1
        self.used_order[key] = len(self.used_order)

    def _find_discard_key(self):
        """Finds the key to discard based on the LFU
        and LRU policies"""
        min_freq = min(self.frequency_count.values())
        candidates = [key for key, freq in self.frequency_count.items(
            ) if freq == min_freq]
        return min(candidates, key=lambda k: self.used_order[k])
