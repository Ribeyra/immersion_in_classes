class HTMLElement:
    def __init__(self, attributes=None):
        self.attributes = attributes if attributes else {}

    def _stringify_attributes(self):
        print(self.attributes.items())
        line = ''.join(f' {k}="{v}"' for k, v in self.attributes.items())
        return line


class HTMLPairElement (HTMLElement):
    def __init__(self, attr):
        super().__init__(attr)
        self.body = ''

    def set_text_content(self, body):
        self.body = body

    def get_text_content(self):
        return self.body

    def get_string_attr(self):
        list_attr = [
            f' {key}="{value}"' for key, value in self.attributes.items()
        ]
        return ''.join(list_attr)

    def get_tag(self):
        return self.tag

    def __str__(self):
        tag = self.get_tag()
        string_attr = self.get_string_attr()
        body = self.get_text_content()
        return f'<{tag}{string_attr}>{body}</{tag}>'


class HTMLDivElement(HTMLPairElement):
    tag = 'div'


div = HTMLDivElement({'name': 'div', 'data-toggle': 'true'})
print(div.get_text_content())
div.set_text_content('Body Text')
print(div.get_text_content())  # Body Text
print(div)  # => '<div name="div" data-toggle="true">Body Text</div>'
