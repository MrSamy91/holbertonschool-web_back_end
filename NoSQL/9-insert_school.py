#!/usr/bin/env python3
""" Inserts new doc in collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Return a new id"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id