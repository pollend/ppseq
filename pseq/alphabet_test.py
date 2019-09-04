import unittest
from pseq.alphabet import Pairing

class PairingTest(unittest.TestCase):
    def testPairing(self):
        pair = Pairing("acgtnxACGTNX-","tgcanxTGCANX-")
        print(pair['a'])

        # self.assertEqual(pair['a'], 't')


if __name__ == '__main__':
    unittest.main()
