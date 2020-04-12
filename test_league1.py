import unittest
import league1

class TestLeague(unittest.TestCase):
    def setUp(self):
        pass
    def test_page_to_soup(self):
        self.assertTrue(len(league1.page_to_soup()) > 0)
    def test_table_data(self):
        soup = league1.page_to_soup()
        self.assertTrue(len(league1.table_data(soup))>10)
            
if __name__ == '__main__':
    unittest.main()