import os
import json
import random


class FileManager:
    """Handle local file system IO."""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class Epithet:
    """ Create epithet """

    vocab = Vocabulary()

    @classmethod
    def create_epithet(self, path, *args, **kwargs):
        """ get and return three words """
        (col_data, col_headers) = self.vocab.from_file(path, *args, **kwargs)
        result = ''
        for col in sorted(col_headers):
            result += random.choice(col_data[col]) + ' '
        return result

    @classmethod
    def get_epithets(self, path, number=1, *args, **kwargs):
        """ create and return number of epithets """
        result = []
        for i in range(number):
            result.append(self.create_epithet(path, *args, **kwargs))
        return result
