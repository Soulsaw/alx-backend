#!/usr/bin/env python3
"""Doc module"""


def index_range(page, page_size):
    """This function return a tuple of"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
