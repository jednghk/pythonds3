class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """takes the key, hashes it, checks for empty hash value and if empty, fill, elif not empty, rehash, elif
        key is equal to key in hash table, replace data value"""
        hash_value = self.hash_function(key, self.size)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, self.size)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(hash_value, self.size)

                if self.slots[next_slot] == key:
                    self.data[next_slot] = data
                else:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_value, size):
        return (old_value+1) % size

    def get(self, key):
        """checks of key is present in hash value slot, then returns the data. If using chaining, go down chain to
        see if key is present, else if rehashing, rehash and check until found"""
        start_slot = self.hash_function(key, len(self.slots))
        position = start_slot

        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    return None

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.put(key, value)

h = HashTable()
h[77] = "bird"
h[44] = "goat"
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[31] = "cow"
print(h.slots)
print(h.data)
'''
h[55] = "pig"
h[20] = "chicken"'''