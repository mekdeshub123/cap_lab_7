import unittest 
from unittest import TestCase
from unittest.mock import patch 

import exchange_rate

class TestExchangeRates(TestCase):

    @patch('exchange_rate.request_rates')
    def test_dollars_to_target(self, mock_rates):
        mock_rate = 12.34567   # Any number will do.  
        example_api_response = {'base': 'USD', 'date': '2019-02-04', 'rates': {'EUR': mock_rate}}  
        mock_rates.side_effect = [ example_api_response ] 
        # 100 dollars is 1234.567 Euros at this made up exchange rate 
        converted = exchange_rate.convert_dollars_to_target(100, 'EUR')
        self.assertEqual(1234.567, converted)

    @patch('exchange_rate.request_rates')
    def test_request_rates(self, mock_rate):
        mock_rate = 15.00
        example_api_response = {'base': 'USD', 'date': '2019-02-04', 'rates': {'EUR':mock_rate}}
        mock_rate.side_effect = [example_api_response]
        converted = exchange_rate.convert_dollars_to_target(100, 'EUR')
        self.assertEqual(15.00, converted)



if __name__ == '__main__':
    unittest.main()
