# -*- coding: utf-8 -*-
import unittest
import os
from qifparse.parser import QifParser

filename = os.path.join(os.path.dirname(__file__), 'file.qif')
filename2 = os.path.join(os.path.dirname(__file__), 'transactions_only.qif')


class TestQIFParsing(unittest.TestCase):

    def testParseFile(self):
        with open(filename) as f:
            qif = QifParser.parse(f)
            self.assertTrue(qif)

    def testWriteFile(self):
        with open(filename) as f:
            data = f.read()
            with open(filename) as ff:
                qif = QifParser.parse(ff)
                #        out = open('out.qif', 'w')
                #        out.write(str(qif))
                #        out.close()
                self.assertEqual(data, str(qif))

    def testParseTransactionsFile(self):
        with open(filename2) as f:
            data = f.read()
            with open(filename2) as ff:
                qif = QifParser.parse(ff)
                #        out = open('out.qif', 'w')
                #        out.write(str(qif))
                #        out.close()
                self.assertEqual(data, str(qif))

if __name__ == "__main__":
    import unittest
    unittest.main()
