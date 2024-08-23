#!/usr/bin/env python3
"""
Log stats
"""

from pymongo import MongoClient


def log_stats():
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Number of logs
    num_logs = collection.count_documents({})
    print(f"{num_logs} logs")

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        num_method = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {num_method}")

    # Status check
    num_status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{num_status_check} status check")


if __name__ == "__main__":
    log_stats()
