from typing import MutableSequence, Sequence


class HashTable:

    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, val):

        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


class Bar:

    def __init__(self, size):
        self.size = size
        self.buckets = self.create_buckets(size)

    @staticmethod
    def create_buckets(size) -> MutableSequence[Sequence[int, int]]:
        return [() for _ in range(size)]

    def set_value(self, key, value):
        key_hash = hash(key) % self.size

        for index, item in enumerate(self.buckets):
            item_key, item_value = item

            if item_key == key_hash:
                self.buckets[index] = (item_key, value)
                return

        self.buckets.append([key_hash, value])

    def get_value(self, key) -> int:
        key_hash = hash(key) % self.size

        for index, item in enumerate(self.buckets):
            item_key, item_value = item

            if item_key == key_hash:
                return self.buckets[index][1]

        return 0

    def delete_value(self, key):
        key_hash = hash(key) % self.size

        for index, item in enumerate(self.buckets):
            item_key, item_value = item

            if item_key == key_hash:
                self.buckets.pop(index)

    def __str__(self):
        return "".join((str(value) for key, value in self.buckets))


if __name__ == '__main__':
    hash_table = HashTable(50)

    # insert some values
    hash_table.set_val('gfg@example.com', 'some value')
    print(hash_table)
    print()

    hash_table.set_val('portal@example.com', 'some other value')
    print(hash_table)
    print()

    # search/access a record with key
    print(hash_table.get_val('portal@example.com'))
    print()

    # delete or remove a value
    hash_table.delete_val('portal@example.com')
    print(hash_table)
