import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_where_list_is_empty(self):
        ''' Test the stock price summary where the price list is empty'''
        
        expected = (0, 0)
        actual = a1.stock_price_summary([])
        self.assertEqual(expected, actual)

    def test_stock_price_where_list_is_zero(self):
        ''' Test the stock price summary where the price list is [0]'''

        expected = (0, 0)
        actual = a1.stock_price_summary([0])
        self.assertEqual(expected, actual)

    def test_stock_price_where_list_is_zero_zero(self):
        ''' Test the stock price summary where the price list is [0, 0]'''    
        
        expected = (0, 0)
        actual = a1.stock_price_summary([0, 0])
        self.assertEqual(expected, actual)

    def test_stock_price_where_list_is_one_gain(self):
        ''' Test the stock price summary where the price list is [.01]'''    
        
        expected = (.01, 0)
        actual = a1.stock_price_summary([.01])
        self.assertEqual(expected, actual)

    def test_stock_price_where_list_is_one_loss(self):
        ''' Test the stock price summary where the price list is [-.01]'''    
        
        expected = (0, -.01)
        actual = a1.stock_price_summary([-.01])
        self.assertEqual(expected, actual)

    def test_stock_price_where_list_has_only_gains(self):
        ''' Test the stock price summary where the price list is [.01, .05, .16, .06]'''    
        
        expected = (.28, 0)
        actual = a1.stock_price_summary([.01, .05, .16, .06])
        self.assertEqual(expected, actual)

    def test_stock_price_where_list_has_only_losses(self):
        ''' Test the stock price summary where the price list is [-.01, -.05, -.16, -.06]'''    
        
        expected = (0, -.28)
        actual = a1.stock_price_summary([-.01, -.05, -.16, -.06])
        self.assertEqual(expected, actual)

    def test_stock_price_where_list_has_multiple_gains_and_losses(self):
        ''' Test the stock price summary where the price list is [.01, -.16, .06, -.04, .08]'''    
        
        expected = (.15, -.2)
        actual = a1.stock_price_summary([.01, -.16, .06, -.04, .08])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)