#!/usr/bin/env python3
""" Pagination helper function."""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Retrieves index range from a give page & page size."""

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
