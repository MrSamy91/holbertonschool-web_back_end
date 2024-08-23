#!/usr/bin/env python3
""" function that changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ update all topics """
    given_name = {"name": name}
    new_topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(given_name, new_topics)
