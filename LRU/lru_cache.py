class lru_cache:
    def _init_(self, size):
        self.size = size
        self.cache = {}
        self.lru = []

# required methods:   put, get and get_cache

    def put(self, key):
        if (len(self.lru) < self.size):
            if key in self.lru:
                self.lru.remove(key)
                self.lru.append(key)
                self.cache[key] = str(key)
            else:
                self.lru.append(key)
                self.cache[key] = str(key)
        else:
            x = self.lru.pop(0)
            self.lru.append(key)
            del self.cache[x]
            self.cache[key] = str(key)

    def get(self, key):
        if key in self.lru:
            return self.cache[key]
        else:
            return None

    def get_cache(self):
        l = []
        for key in reversed(self.lru):
            l.append(key + "=" + self.cache[key])
        return l
