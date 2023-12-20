import unittest
from main import get_name, get_directory, add_person, yaApi_create_folder


class TestSecretary(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual(get_name('10006'), 'Аристарх Павлов')
    def test_get_directory(self):
        self.assertEqual(get_directory('10006'), 2)
    def test_add_person(self):
        self.assertEqual(add_person('passport','470011', 'test', 3), True)
class TestYa_api(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(yaApi_create_folder('test'), 201)
