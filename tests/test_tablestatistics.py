import unittest
from pzbasket.tablestatistic import TableStatistics


class TableStatisticsTests(unittest.TestCase):
    def test_construktor(self):
        api_client = TableStatistics('d3')
        self.assertTrue(api_client is not None)
        
    def test_data(self):
        api_client = TableStatistics('d3')
        api_client.data()
        self.assertTrue(len(api_client.table_data) > 0)
        
        
    def test_show_data(self):
        api_client = TableStatistics('d3')
        api_client.data()
        