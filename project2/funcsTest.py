import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):


   def testUpdateAcceleration(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)

   def test1UpdateAcceleration(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 9), 1.296)

   def test2UpdateAcceleration(self):
      self.assertAlmostEqual(updateAcceleration(-1.62, 9), -1.296)


   def testUpdateAltitude(self):
      self.assertAlmostEqual(updateAltitude(100.05, 20.6, 1.62), 121.46)

   def test1UpdateAltitude(self):
      self.assertAlmostEqual(updateAltitude(50, 10, 1.296), 60.648)
      

   def testUpdateVelocity1(self):
      self.assertAlmostEqual(updateVelocity(50.23, 50.23), 100.46)

   def test1UpdateVelocity1(self):
      self.assertAlmostEqual(updateVelocity(20.5, 22.25), 42.75)


   def testUpdateFuel(self):
      self.assertAlmostEqual(updateFuel(5, 1), 4)

   def test1UpdateFuel(self):
      self.assertAlmostEqual(updateFuel(10, 9), 1)

   #def testgetFuelRate(self):
     # self.assertAlmostEqual(getFuelRate(9),9)

   #def testgetFuelRate(self):
      #self.assertAlmostEqual(getFuelRate(5),5)


   #def testdisplayLMLandingStatus(self):
 #     self.assertAlmostEqual(displayLMLandingStatus(0), "Status at landing - The eagle has landed!")



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

