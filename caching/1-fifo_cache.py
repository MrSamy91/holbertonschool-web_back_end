#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()
        self.queue = []  # Pour garder l'ordre d'insertion

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Si le cache est plein et la clé n'existe pas déjà
                first_key = self.queue.pop(0)  # Retire le premier élément
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
            
            self.cache_data[key] = item
            if key not in self.queue:
                self.queue.append(key)  # Ajoute la nouvelle clé à la fin

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None