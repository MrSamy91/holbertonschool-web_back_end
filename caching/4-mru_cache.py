#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.usage_order = []  # Pour suivre l'ordre d'utilisation

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            # Si la clé existe déjà, la mettre à jour
            if key in self.cache_data:
                self.usage_order.remove(key)
            # Si le cache est plein et c'est une nouvelle clé
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.usage_order.pop()  # Retire le plus récemment utilisé
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")
            
            # Ajoute/Met à jour l'élément
            self.cache_data[key] = item
            self.usage_order.append(key)  # Ajoute à la fin car le plus récent

    def get(self, key):
        """ Get an item by key and update usage
        """
        if key is not None and key in self.cache_data:
            # Met à jour l'ordre d'utilisation
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None