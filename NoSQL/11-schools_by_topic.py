#!/usr/bin/env python3
""" return the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ school list """
    documents = mongo_collection.find({"topics": topic})
    return [item for item in documents]
