import sys
sys.path.append('.')
sys.path.append('..')

import unittest
import shaolin
import pilas

class TestEjemplo(unittest.TestCase):

    def testShaolin(self):
        pilas.iniciar()
        s = shaolin.Shaolin()
        pilas.terminar()

if __name__ == '__main__':
    unittest.main()

