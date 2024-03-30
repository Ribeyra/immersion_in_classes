class Base:
    def __init__(self):
        pass

    def is_instance_of(self, name):
        list_of_class_names = [
            class_name.__name__ for class_name in self.__class__.__mro__
        ]
        return name in list_of_class_names


class Child(Base):
    pass


class ChildOfChild(Child):
    pass


obj = ChildOfChild()
print(obj.is_instance_of('Base'))           # True
print(obj.is_instance_of('Child'))          # True
print(obj.is_instance_of('ChildOfChild'))   # True
print(obj.is_instance_of('SomeClass'))      # False
