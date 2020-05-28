class lru_cache:
    def _init_(self, size):
        self.size = size
        self.cache = {}
        self.lru = []
    # required methods:   put, get and get_cache
