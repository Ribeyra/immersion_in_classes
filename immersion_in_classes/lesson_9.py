from abc import ABC, abstractmethod


""" class HTMLElement(ABC):
    def __init__(self, attributes={}):
        self.attributes = attributes

    def get_attribute(self, key):
        return self.attributes.get(key)

    def __str__(self):
        return f'This is inst of {self.__class__.__name__} class'


x = HTMLElement()
print(x)    # This is inst of HTMLElement class """


""" class Showable(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Greeter(Showable):
    def __init__(self, name):
        self.name = name


class Goodbyer(Greeter):
    def __str__(self):
        return f'Goob bye, {self.name}!'


x = Goodbyer('John Cena')
print(x)    # Goob bye, John Cena! """


class HTMLElement(ABC):
    ATTRIBUTE_NAMES = ['name', 'class']

    def __init__(self, attributes=None):
        if attributes is None:
            self.attributes = {}
        else:
            self.attributes = attributes

    @classmethod
    def get_attribute_names(cls):
        return cls.ATTRIBUTE_NAMES

    def get_attributes(self):
        return self.attributes

    # BEGIN (write your solution here)
    @abstractmethod
    def is_valid():
        pass
    # END


class HTMLImgElement(HTMLElement):
    ATTRIBUTE_NAMES = ['src']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
        img_attr = self.get_attribute_names()
        return all(map(lambda x: x in img_attr, self.get_attributes()))
    # END


class HTMLButtonElement(HTMLElement):
    ATTRIBUTE_NAMES = ['type']
    TYPE_NAMES = ['button', 'submit', 'reset']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
        button_attr = self.get_attribute_names()
        type_attr = False
        available_val = ('button', 'submit', 'reset')
        for attr_name, attr_value in self.attributes.items():
            if attr_name not in button_attr:
                return False
            elif attr_name == 'type' and attr_value in available_val:
                type_attr = True
        return type_attr
    # END


img1 = HTMLImgElement({'class': 'rounded', 'src': 'path/to/image'})
print(img1.is_valid())  # True

img2 = HTMLImgElement({'class': 'rounded', 'href': 'path/to/image'})
print(img2.is_valid())  # False

button1 = HTMLButtonElement({'class': 'rounded', 'type': 'button'})
print(button1.is_valid())  # True

button2 = HTMLButtonElement({'class': 'rounded'})
print(button2.is_valid())  # False
