#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve a hypermedia paginated subset of the dataset
        based on the provided index and page_size.

        Returns:
            Dict: A dictionary containing info about the paginated subset
        """
        assert index is None or (isinstance(index, int) and 0 <= index < len(
            self.__indexed_dataset)), "index out of range"
        assert isinstance(page_size, int) and page_size > 0

        adjusted_index = index
        for i in range(index, len(self.__indexed_dataset)):
            if i in self.__indexed_dataset:
                adjusted_index = i
                break

        start_index = adjusted_index if index is not None else 0
        end_index = start_index + page_size
        dataset_length = len(self.__indexed_dataset)

        if start_index >= dataset_length or start_index < 0:
            return {
                    "index": start_index,
                    "data": [],
                    "page_size": page_size,
                    "next_index": None,
            }

        data_page = [self.__indexed_dataset[i] for i in range(
            start_index, min(end_index, dataset_length))]

        next_index = end_index if end_index < dataset_length else None

        return {
                "index": start_index,
                "data": data_page,
                "page_size": page_size,
                "next_index": next_index,
        }
