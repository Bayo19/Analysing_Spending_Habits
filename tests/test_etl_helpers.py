import unittest
import sys
sys.path.append("c:\\Users\\Bayo's Computer\\Desktop\\WebsiteFiles\\bank_project\\")
import src.etl_helper as e_helper


class TestEtlHelper(unittest.TestCase):
    def setUp(self):
        self.d1 = {'first': 1, 'second': 2}
        self.d2 = {'third': 3, 'fourth': 4}
        self.d3 = {'fifth': 5, 'sixth': 6, 'seventh': 7}
        
    def test_delete_column(self):
        self.assertEqual(e_helper.delete_column(self.d1, 'first'), {'second': 2}) 
        self.assertEqual(e_helper.delete_column(self.d2, 'fourth'), {'third': 3}) 
        self.assertEqual(e_helper.delete_column(self.d3, 'sixth'), {'fifth': 5, 'seventh': 7})
        
    def test_format_date(self):
        self.assertEqual(e_helper.format_date_postgres('29/09/2021'), '09/29/2021')
        self.assertEqual(e_helper.format_date_postgres('11/10/1991'), '10/11/1991')
        self.assertEqual(e_helper.format_date_postgres('13/12/2001'), '12/13/2001')
    
    def test_get_month_from_date(self):
        self.assertEqual(e_helper.get_month_from_date('11/10/1991'), 'October')
        self.assertEqual(e_helper.get_month_from_date('12/6/2017'), 'June')
        self.assertEqual(e_helper.get_month_from_date('19/02/1922'), 'February')
        self.assertEqual(e_helper.get_month_from_date('27/12/1896'), 'December')
        
    def test_get_season_from_month(self):
        self.assertEqual(e_helper.get_season_from_month('October'), 'Autumn')
        self.assertEqual(e_helper.get_season_from_month('January'), 'Winter')
        self.assertEqual(e_helper.get_season_from_month('July'), 'Summer')
        
    def test_delete_duplicates(self):
        self.assertEqual(e_helper.delete_duplicates([1,3,6,9,12,3,5,7]), [1,3,6,9,12,5,7])
        self.assertEqual(e_helper.delete_duplicates(['a', 'b', 'd', 'a', 'f']), ['a', 'b', 'd', 'f'])
        self.assertEqual(e_helper.delete_duplicates([{'third': 3}, {'fourth': 4}, {'third': 3}, {'ninth': 9}]),
                                                    [{'third': 3}, {'fourth': 4}, {'ninth': 9}])

if __name__ == '__main__':
    unittest.main()  

