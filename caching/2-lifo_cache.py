#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()
        self.stack = []  # Pour garder l'ordre d'insertion

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # Si le cache est plein et la clé n'existe pas déjà
                last_key = self.stack.pop()  # Retire le dernier élément
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            
            if key in self.cache_data:
                self.stack.remove(key)
            self.cache_data[key] = item
            self.stack.append(key)  # Ajoute la nouvelle clé à la fin

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None