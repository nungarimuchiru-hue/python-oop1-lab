#!/usr/bin/env python3

class Book:
    def __init__(self,title,author,total_pages):
        self.title = title
        self._author = author
        self._total_pages = total_pages

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def total_pages(self):
        return self._total_pages    