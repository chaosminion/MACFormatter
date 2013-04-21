import unittest
from macformatter import *

class TestMACFormatConverterResult(unittest.TestCase):
    '''
    The purpose of these test is to test the logic of format conversion.
    '''

    def test_address_with_no_delimiters(self):

        self.result = ['001122334455']
        for test in self.result:
            MACAddress = address_with_no_delimiters(test)
            self.assertIs(len(MACAddress), 17,
                          "The address is not 17 characters.")
            print("address_with_no_delimiters", MACAddress)

    def test_address_with_periods(self):

        self.result = ('0011.2233.4455', 'abcd.ef01.0123')
        for test in self.result:
            MACAddress = address_with_periods(test)
            print('address_with_periods', MACAddress)
            self.assertIs(MACAddress[2], ':', 'Incorrect delimiter detected!')

    def test_convert(self):
        self.result = ('0011223344556', '01234567890123456')
        for unformatedMACAddress in self.result:
            print('test_convert', unformatedMACAddress)
            self.assertFalse((len(unformatedMACAddress) > 18) and
                             (self.answerLabel['text'] != ''), 'The input is too long!')

    def test_four_delimiters(self):
        '''
        Convert any delimiter including spaces to colins.
        '''
        self.result = ("00 11 22 33 44 55", "00*11*22*33*44*55")

        for each in self.result:
            self.assertTrue(len(self.result), 17)
            self.assertTrue(self.result[2::3], "::::")

if __name__ == '__main__':
    unittest.main()
