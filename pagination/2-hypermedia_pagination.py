#!/usr/bin/env python3
"""Simple pagination"""

import csv
import math
from typing import List, Tuple

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset
        """
        assert isinstance(page, int) is True
        assert isinstance(page_size, int) is True
        assert page > 0
        assert page_size > 0
        pag_indexes = index_range(page=page, page_size=page_size)
        self.dataset()
        return self.__dataset[pag_indexes[0]: pag_indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a dictionnary
        """
        data = self.get_page(page, page_size)
        total = math.ceil(len(self.__dataset) / page_size)
        next = page + 1 if page < total else None
        prev = page - 1 if page > 1 else None
        return {'page_size': len(data), 'page': page, 'data': data,
                'next_page': next, 'prev_page': prev, 'total_pages': total}
