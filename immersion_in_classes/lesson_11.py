from lxml import etree


class Sanitizer:
    # BEGIN (write your solution here)
    def sanitize(self, text):
        return text.strip()
    # END


def strip_tags(tag_string):
    parser = etree.HTMLParser()
    tree = etree.fromstring(tag_string, parser)
    return etree.tostring(tree, encoding='unicode', method='text')


class SanitizerStripTagsDecorator:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer

    # BEGIN (write your solution here)
    def sanitize(self, text):
        tags_free_text = strip_tags(text)
        res = self.sanitizer.sanitize(tags_free_text)
        return res
    # END


""" base_sanitizer = Sanitizer() """
# передаем в обертку объект base_sanitizer
sanitizer = Sanitizer()
print(f'"{sanitizer.sanitize("text   ")}"')  # 'text'
print(f'"{sanitizer.sanitize(" boom ")}"')  # 'boom'
