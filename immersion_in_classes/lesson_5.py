""" class HTMLSelectElement:
    def __init__(self, options):
        self.options = options

    def item(self, index):
        return self.options[index]


class HTMLCustomSelectElement(HTMLSelectElement):
    def item(self, index):
        if index < 0 or index >= len(self.options):
            return "Ошибка: индекс вне диапазона"
        return super().item(index)


custom_options = HTMLCustomSelectElement(["Opt 1", "Opt 2", "Opt 3"])
print(custom_options.item(1))  # "Opt 2"
print(custom_options.item(3))  # "Ошибка: индекс вне диапазона"

select = HTMLCustomSelectElement(["Opt 1", "Opt 2", "Opt 3"])
# Этот вызов всегда относится к методу item, переопределенному внутри
# HTMLCustomSelectElement
# Вызвать item напрямую из HTMLSelectElement невозможно
print(select.item(3))
print(select._HTMLSelectElement__item(3))   # AttributeError
print(select.super().item(3))               # AttributeError """


import os

""" stats = os.stat('/etc/hosts')
print(stats.st_size)  # размер в байтах """


class FileInfo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_stat = os.stat('/etc/hosts')

    def get_size(self):
        return self.file_stat.st_size


class SmartFileInfo(FileInfo):
    units = {'b': 1, 'kb': 1024}

    def get_size(self, unit='b'):
        if unit not in self.units:
            raise ValueError('ValueError')
        raw_size = super().get_size()
        return raw_size / self.units[unit]


file_stat = SmartFileInfo('Makefile')
print(file_stat.get_size())  # 67
print(file_stat.get_size('b'))  # 67
print(file_stat.get_size('kb'))  # 0.0654296875
print(file_stat.get_size('udav'))  # ValueError
