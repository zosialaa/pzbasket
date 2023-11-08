import unittest
from pzbasket.teamstatistics import Teamstatistics


class TeamStatisticsTests(unittest.TestCase):
    def test_construktor(self):
        api_client2 = Teamstatistics('2659')
        self.assertTrue(api_client2 is not None)
        
    def test_data(self):
        api_client2 = Teamstatistics('2659')
        api_client2.data()
        self.assertTrue(len(api_client2.table_data) > 0)
        
        
    def test_show_data(self):
        api_client2 = Teamstatistics('2659')
        api_client2.data()