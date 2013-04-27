#!/usr/bin/python3
'''
The following are tests for macformatter.py
'''
import unittest
from macformatter import *

class TestMACFormatConverterResult(unittest.TestCase):
    '''
    The purpose of these test is to test the logic of format conversion.
    '''
    def test_address_with_no_delimiters(self):
        '''
        Convert MAC address with no delimiters
        '''
        self.result = ['001122334455']
        for test in self.result:
            mac_address = address_with_no_delimiters(test)
            self.assertIs(len(mac_address), 17,
                          "The address is not 17 characters.")
            print("address_with_no_delimiters", mac_address)

    def test_address_with_periods(self):
        '''
        Remove the two period delimiters and seperate octect pairs
        with colons.
        '''
        self.result = ('0011.2233.4455', 'abcd.ef01.0123')
        for test in self.result:
            mac_address = address_with_periods(test)
            print('address_with_periods', mac_address)
            self.assertIs(mac_address[2], ':', 'Incorrect delimiter detected!')

    def test_convert(self):
        '''
        Test the input?  This method may have to be reconsidered.
        Is this needed?
        '''
        self.result = ('0011223344556', '01234567890123456')
        for unformatedmac_address in self.result:
            print('test_convert', unformatedmac_address)
            self.assertFalse((len(unformatedmac_address) > 18) and
                             (self.answerLabel['text'] != ''), 'The\
                             input is too long!')

    def test_five_delimiters(self):
        '''
        Convert any delimiter including spaces to colins.
        '''
        self.test = ("00 11 22 33 44 55", "00*11*22*33*44*55", \
                     "01.23.45.67.89.10")

##        import pdb; pdb.set_trace()

        for test in self.test:
            self.result = five_delimiters(test)
            self.assertTrue(self.result[2::3], "::::")

if __name__ == '__main__':
    unittest.main()
