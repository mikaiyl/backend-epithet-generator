from helpers import Vocabulary, Epithet
from unittest import TestCase, expectedFailure


class TestHelpers(TestCase):

    def setUp(self):
        ''' Create instance of Vocabulary class '''
        self.vocab = Vocabulary()
        self.assertTrue(self.vocab)

    def test_ext(self):
        ''' Test Vocabulary.get_extension() '''
        self.assertEquals(self.vocab.files.get_extension('file.ext'), 'ext')
        self.assertNotEquals(self.vocab.files.get_extension('text.txt'), 'ext')

    def test_read_json(self):
        ''' Test json read works and returns dictionary '''
        json = self.vocab.files.read_json('../../resources/data.json')
        self.assertTrue(json)
        self.assertEquals(type(json), dict)

    def test_normalize_json(self):
        ''' Test that data is imported in correct representation '''
        data = self.vocab.from_json('../../resources/data.json', fields=True)
        self.assertEquals( (type(data[0]), type(data[1])), ( dict, list )) # noqa

    def test_normalize_file(self):
        ''''''
        pass

    def test_normalize_stratigies(self):
        ''' test returns strategy '''
        self.assertEquals(self.vocab.strategies('json'), self.vocab.from_json)

    @expectedFailure
    def test_normalize_stratigies_expected_to_fail(self):
        ''' test returns strategy '''
        self.fail(self.vocab.strategies('csv'), self.vocab.from_json) # noqa

    def test_create_epithet(self):
        """ Test Epithet class """
        self.assertTrue(Epithet.create_epithet('../../resources/data.json').count(' ') > 2) # noqa
        self.assertEquals(str(type(Epithet.create_epithet('../../resources/data.json'))), "<type 'unicode'>") # noqa

    def test_epithets(self):
        """ Test Epithet class """
        self.assertEquals(len(Epithet.get_epithets('../../resources/data.json',20)), 20) # noqa

    def test_random(self):
        """ Test Epithet class """
        self.assertTrue(len(Epithet.get_random('../../resources/data.json',ceil=20)) < 20) # noqa
