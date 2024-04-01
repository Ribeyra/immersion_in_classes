class GoogleStorage:
    def __init__(self):
        self.elements = {}

    # BEGIN (write your solution here)
    def set(self, key, value):
        self.elements[key] = value

    def get(self, key):
        return self.elements.get(key)

    def count(self):
        raise Exception
    # END


storage = GoogleStorage()
storage.set('one', 'two')
print(storage.get('one'))  # 'two'
storage.count()  # Exception
