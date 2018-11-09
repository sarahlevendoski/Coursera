import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """
    
    def test_num_buses_where_n_is_0(self):
        ''' Test num_buses where there are 0 people transported'''

        expected = 0
        actual = a1.num_buses(0)
        self.assertEqual(expected, actual)
    
    def test_num_buses_where_n_is_49(self):
        ''' Test num_buses where there are 49 people transported'''
        
        expected = 1
        actual = a1.num_buses(49)
        self.assertEqual(expected, actual)    
    
    def test_num_buses_where_n_is_50(self):
        ''' Test num_buses where there are 50 people transported'''

        expected = 1
        actual = a1.num_buses(50)
        self.assertEqual(expected, actual)
    
    def test_num_buses_where_n_is_51(self):
        ''' Test num_buses where there are 51 people transported'''
        
        expected = 2
        actual = a1.num_buses(51)
        self.assertEqual(expected, actual)
    
    def test_num_buses_where_n_is_105(self):
        ''' Test num_buses where there are 105 people transported'''

        expected = 3
        actual = a1.num_buses(105)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)