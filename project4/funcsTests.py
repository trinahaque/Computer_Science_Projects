#Project3 Tests

import unittest
from funcs import *

class TestCases(unittest.TestCase):
 #   amy = "CALPOLY: (DOWN) row: 1 column: 0"
 #   input_string = 'WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
    new_list = ['WAQHGTTWEE',
'CBMIVQQELS', 'AZXWKWIIIL',
'LDWLFXPIPV', 'PONDTMVAMN',
'OEDSOYQGOB', 'LGQCKGMMCT',
'YCSLOACUZM',
'XVDMGSXCYZ',
'UUIUNIXFNU']
 #   new_list = ['LLARSHAHLC', 'AOOLLAMILL', 'OIDNALHGIH', 'RBAMCETUHS', 'SMOSKAGETR', 'CORCHORROA', 'IDBSLSAAOM','IGOSMONDFL', 'HHNGMSDCMA','CMIRRSMLHP']

##    def testinput_puzzle():
##        self.assertAlmostEqual(input_puzzle(self.input_string), self.new_list)
        
    def testforward(self):
        self.assertAlmostEqual(forward(self.new_list, 'UNIX')[0], 9)
        self.assertAlmostEqual(forward(self.new_list, 'UNIX')[1], 3)

    def test1forward(self):
        self.assertAlmostEqual(forward(self.new_list, 'SLO'), (7,2))

##   def test2UpdateAcceleration(self):
##      self.assertAlmostEqual(backward(-1.62, 9), -1.296)


    def testbackward(self):
        self.assertAlmostEqual(backward(self.new_list, 'VIM'), (1,4))

    def testup(self):
        self.assertAlmostEqual(up(self.new_list, 'COMPILE'), (6,8))

    def testup(self):
        self.assertAlmostEqual(down(self.new_list, 'CALPOLY'), (1,0))

##    def testcheck_everything(self):
##        self.assertAlmostEqual(check_everything(self.new_list, 'CALPOLY'), self.amy)

##   def test1backward(self):
##      self.assertAlmostEqual(backward(50, 10, 1.296), 60.648)
      

##   def testUpdateVelocity1(self):
##      self.assertAlmostEqual(updateVelocity(50.23, 50.23), 100.46)
##
##   def test1UpdateVelocity1(self):
##      self.assertAlmostEqual(updateVelocity(20.5, 22.25), 42.75)
##
##
##   def testUpdateFuel(self):
##      self.assertAlmostEqual(updateFuel(5, 1), 4)
##
##   def test1UpdateFuel(self):
##      self.assertAlmostEqual(updateFuel(10, 9), 1)

if __name__ == '__main__':
   unittest.main()
#it runs the unit test
