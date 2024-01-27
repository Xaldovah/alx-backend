#!/usr/bin/env python3
"""Pagination module for a database of popular baby names"""
import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server with an empty dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Retrieve the cached dataset, loading it from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a paginated subset of the dataset based on the provided
        page and page_size.

        Args:
            - page (int): The page number to retrieve (default is 1).
            - page_size (int): The number of items per page (default is 10).

            Returns:
                List[List]: The paginated subset of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset_length = len(self.dataset())

        if start_index >= dataset_length or start_index < 0:
            return []

        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """generates a dictionary with the requested pagination information"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
                "page_size": len(page_data),
                "page": page,
                "data": page_data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages,
        }
