#!/usr/bin/env python3
"""This module defines the index_range class."""


def index_range(page: int, page_size: int) -> tuple:
    """
    function that takes two integer arguments page and page_size return a
    tuple of size two containing a start index and
    an end index corresponding to
    the range of indexes to return in a list for those particular
    pagination parameters.
    """
    start_page = page - 1
    return ((page_size * start_page, page_size * page))
