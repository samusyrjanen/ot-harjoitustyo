import unittest
from file_reader import File_reader

class TestFile_reader(unittest.TestCase):
    def setUp(self):
        self.file_reader = File_reader()
        self.file_reader.clear()
    
    def test_read(self):
        self.assertEqual(self.file_reader.read(), [])

    def test_lisaa_tulo(self):
        self.file_reader.lisaa_tulo(10, 'test1')
        self.file_reader.lisaa_tulo(20, 'test2')
        self.assertEqual(self.file_reader.read(), [10, 20])

    def test_clear(self):
        self.file_reader.clear()
        self.assertEqual(self.file_reader.read(), [])