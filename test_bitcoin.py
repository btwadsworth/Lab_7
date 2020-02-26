import unittest 
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestBitcoin(TestCase):

    @patch('bitcoin.get_rate')
    def test_bitcoin_get_rate(self, mock_rates):
        example_api_response = {'bpi': {'USD': {'rate_float' : 123.45}}}
        mock_rates.side_effect = [ example_api_response ]
        rate = bitcoin.get_amount()
        self.assertEqual(12345, rate)


if __name__ == "__main__":
    unittest.main()