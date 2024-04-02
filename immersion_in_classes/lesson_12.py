""" class Mixin1:
    def test(self):
        print("Mixin1")


class Mixin2:
    def test(self):
        print("Mixin2")


class MyClass(Mixin1, Mixin2):
    pass


mc = MyClass()
print(mc.__class__.__mro__)  # Output: Mixin1 """


from abc import ABC, abstractmethod


class Enumerable(ABC):
    @abstractmethod
    def get_iterator(self):
        raise NotImplementedError("Subclasses must implement this method")

    # BEGIN (write your solution here)
    def max_by(self, key):
        return max(self.get_iterator(), key=key, default=None)
    # END
