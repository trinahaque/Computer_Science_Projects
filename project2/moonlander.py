from landerFuncs import *

def main():
   showWelcome()
   altitude = getAltitude()
   fuelAmount = getFuel()
   print("")
   print("LM state at retrorocket cutoff")
   elapsedTime = 0
   velocity = 0
   fuelRate = 0
   acceleration = 0
   gravity = 1.62
 
   
  
   while altitude > 0 and fuelAmount > 0:
   
      displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
      fuelRate = getFuelRate(fuelAmount)
      fuelAmount = fuelAmount - fuelRate
      acceleration = updateAcceleration(gravity, fuelRate)
      y = updateVelocity(velocity, acceleration)
      altitude = updateAltitude(altitude, velocity, acceleration)
      velocity = y
      elapsedTime = elapsedTime + 1
      if altitude <= 0:
         altitude = 0
         

   
   #print("LM state at landing/impact")
   #displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
   #displayLMLandingStatus(velocity)
         

   while altitude > 0 and fuelAmount == 0:
      print("OUT OF FUEL - Elapsed Time:", elapsedTime, "Altitude:", "{0:.2f}".format(round(altitude, 2)), "Velocity: ", "{0:.2f}".format(round(velocity, 2)))
      elapsedTime = elapsedTime + 1
      fuelRate = 0
      acceleration = -1.62
      altitude = updateAltitude(altitude, velocity, acceleration)
      velocity = updateVelocity(velocity, acceleration)
      if altitude <= 0:
        altitude = 0
        break
   print("")
   print("LM state at landing/impact")
   displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
   print("")
   displayLMLandingStatus(velocity)

   
      
      

      
 

if __name__ == '__main__':
   main()

#LM state at landing/impact(last)
#LM state at retrorocket cutoff (first)
# none in the body
