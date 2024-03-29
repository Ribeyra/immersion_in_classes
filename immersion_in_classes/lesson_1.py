class HTMLElement:
    def __init__(self, attributes=None):
        self.attributes = attributes if attributes else {}

    # BEGIN (write your solution here)
    def _stringify_attributes(self):
        res = [f'{key}="{value}"' for key, value in self.attributes.items()]
        return ' '.join(res)
    # END


class HTMLHrElement(HTMLElement):
    def __str__(self):
        str_attr = self._stringify_attributes()
        if str_attr:
            return f'<hr {str_attr}>'
        return '<hr>'
