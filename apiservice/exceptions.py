class PageOutOfRangeException(Exception):
    def __init__(self, page, max_pages, message="Page out of range:"):
        self.message = message + f" requested={page} page_range= <1, {max_pages}>"
        super().__init__(self.message)


class InvalidPageSizeException(Exception):
    def __init__(self, page_size, message="Invalid page size: "):
        self.message = message + str(page_size)
        super().__init__(message)
