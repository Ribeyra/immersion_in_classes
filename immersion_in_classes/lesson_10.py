""" class BaseEntity:
    def get_table(self):
        return self._table


class User(BaseEntity):
    _table = 'users'


x = User()
print(x.get_table())  # NameError: name '_table' is not defined """


class HTMLElement:
    def __init__(self):
        self.body = None

    def set_text_content(self, body):
        self.body = body

    # BEGIN (write your solution here)
    def __str__(self):
        params = self.get_params()
        name = params["name"]
        body = self.body
        pair = params['pair']
        tag = f'<{name}>'
        res = tag if not body else tag + body
        return res if not pair else res + f'</{name}>'
    # END


""" class HTMLDivElement(HTMLElement):  # тупая версия решения
    # BEGIN (write your solution here)
    _params1 = {
        'name': 'div',
        'pair': True
    }

    def get_params(self):
        return self._params1

    @property
    def _params(self):
        return self._params1

    @_params.setter
    def _params(self, value):
        pass
    # END """


class HTMLDivElement(HTMLElement):
    # BEGIN (write your solution here)
    _params = {
        'name': 'div',
        'pair': True
    }

    @classmethod
    def get_params(cls):
        return cls._params
    # END


element = HTMLDivElement()
element.set_text_content('hello!')
print(element)  # => <div>hello!</div>

# установка свойства "в обход" не влияет на параметры
print(element._params)  # => {'name': 'div', 'pair': True}
element._params = {'name': 'foo'}
print(element)   # => <div></div>
