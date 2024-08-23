#!/usr/bin/env python3
""" Define a function index_range """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple with the range start and end index"""
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
