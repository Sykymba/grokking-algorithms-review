import unittest
from Binary_search import binary_search, line_search

class TestSearchAlgorithms(unittest.TestCase):
    """ Класс для тестирования функций поиска"""
    def setUp(self):
        self.my_list = [i for i in range(1, 10000000)]
        self.zero_list = []
        self.one_item_list = [6666]

    #Тесты для бинарного поиска
    def test_binary_search_existing(self):
        self.assertEqual(binary_search(self.my_list, 10000), 10000)
        self.assertEqual(binary_search(self.my_list, 99888), 99888)
        self.assertEqual(binary_search(self.my_list, 723666), 723666)

    def test_binary_search_not_found(self):
        self.assertEqual(binary_search(self.my_list, 10100000000), -1)
        self.assertEqual(binary_search(self.my_list, 0), -1)

    def test_binary_search_zero_list(self):
        self.assertEqual(binary_search(self.zero_list, 5), -1)

    def test_binary_serarch_one_item(self):
        self.assertEqual(binary_search(self.one_item_list, 6666), 6666)
        self.assertEqual(binary_search(self.one_item_list, 7777), -1)


    #Тесты для линейного поиска
    def test_line_search_existing(self):
        self.assertEqual(line_search(self.my_list, 10000), 10000)
        self.assertEqual(line_search(self.my_list, 99888), 99888)
        self.assertEqual(line_search(self.my_list, 723666), 723666)

    def test_line_search_not_found(self):
        self.assertEqual(line_search(self.my_list, 101000111), -1)
        self.assertEqual(line_search(self.my_list, 0), -1)

    def test_line_search_zero_list(self):
        self.assertEqual(binary_search(self.zero_list, 5), -1)

    def test_line_search_one_item(self):
        self.assertEqual(binary_search(self.one_item_list, 6666), 6666)
        self.assertEqual(binary_search(self.one_item_list, 7777), -1)


if __name__ == '__main__':
    unittest.main()