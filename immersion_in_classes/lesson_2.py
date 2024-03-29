""" class A:
    def __private_method(self):
        print('private method class A')

    def public_method(self):
        self.__private_method()


class B(A):
    def __private_method(self):
        print('private method class B')

    def public_method_b(self):
        self.__private_method()


a = A()
a.public_method()       # private method class A
b = B()
b.public_method()       # private method class A
b.public_method_b()     # private method class B """


""" class User:
    def __init__(self):
        self.name = "User"

    # зададим приватный метод
    def __private_greet(self):
        return f"Hello, {self.name}!"

    # зададим публичный интерфейс для этого метода
    def greet(self):
        return self.__private_greet()


class John(User):
    # попробуем переопределить приватный метод родителя
    def __private_greet(self):
        return "Hello, John!"


# метод не изменился
print(John().greet())   # 'Hello, User!'

# посмотрим весь список методов John с помощью функции dir
# здесь мы видим, что к имени приватных методов для защиты от перезаписи
# добавляется их класс так в наследнике есть оригинальный метод и метод
# наследника
dir(John)   # ['_John__private_greet', '_User__private_greet', ..] """


class HTMLElement:
    def __init__(self, attributes=None):
        if attributes is None:
            self.attributes = {}
        else:
            self.attributes = attributes

    def get_attribute(self, key):
        return self.attributes.get(key)

    # BEGIN (write your solution here)
    def __to_list(self, string):
        return string.split()

    def __to_string(self, lst):
        return ' '.join(lst)

    def add_tag(self, tag):
        tag_list = self.__to_list(self.attributes['tag'])
        if tag not in tag_list:
            tag_list.append(tag)
            self.attributes['tag'] = self.__to_string(tag_list)

    def remove_tag(self, tag):
        tag_list = self.__to_list(self.attributes['tag'])
        if tag in tag_list:
            tag_list.remove(tag)
            self.attributes['tag'] = self.__to_string(tag_list)

    def toggle_tag(self, tag):
        tag_list = self.__to_list(self.attributes['tag'])
        if tag in tag_list:
            tag_list.remove(tag)
            self.attributes['tag'] = self.__to_string(tag_list)
        else:
            tag_list.append(tag)
            self.attributes['tag'] = self.__to_string(tag_list)
    # END


div = HTMLElement({'tag': 'one two'})
print(div.get_attribute('tag'))  # 'one two'

div.add_tag('small')
print(div.get_attribute('tag'))  # 'one two small'

div.add_tag('small')
print(div.get_attribute('tag'))  # 'one two small'

div.remove_tag('two')
print(div.get_attribute('tag'))  # 'one small'

div.toggle_tag('small')
print(div.get_attribute('tag'))  # 'one'

div.toggle_tag('small')
print(div.get_attribute('tag'))  # 'one small'
