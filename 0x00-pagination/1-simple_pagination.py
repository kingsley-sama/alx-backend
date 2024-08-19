#!/usr/bin/env python3
"""This module defines the Server class."""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """class variables"""
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

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        function that takes two integer arguments page and page_size return a
        tuple of size two containing a start index and
        an end index corresponding to
        the range of indexes to return in a list for those particular
        pagination parameters.
        """
        start_page = page - 1
        return ((page_size * start_page, page_size * page))

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page retrieves data in a particular range"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        value_index: tuple = self.index_range(page, page_size)
        start: int = value_index[0]
        stop: int = value_index[1]
        dataset: List[List] = self.dataset()
        if start < 0 or stop > len(dataset) or start >= len(dataset):
            return []
        return dataset[start:stop]
