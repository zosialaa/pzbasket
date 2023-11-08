import unittest
from pzbasket.statistics import Statistics
import io
import contextlib

class StatisticsTests(unittest.TestCase):
    def test_construktor(self):
        api_client1 = Statistics()
        self.assertTrue(api_client1 is not None)
        
    def test_statistics_data(self):
         def test_data(self):
            api_client1 = Statistics()
            api_client1.data()
            self.assertTrue(len(api_client1.table_data) > 0)
        
        
    def test_show_data(self):
        api_client1 = Statistics()
        api_client1.data()
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            api_client1.show_data()
        self.assertTrue(f.getvalue() is not None)