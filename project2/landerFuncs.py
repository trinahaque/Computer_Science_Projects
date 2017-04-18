# Project 2 - Moonlander
# Author: Trina Haque
# Version: 1, Mac Os X
#This is a moonlander project. It takes altitude and initial fuel. Then it calculates the time it takes to reach altitude 0 or fuel 0

def showWelcome():
   print("Welcome aboard the Lunar Module Flight Simulator \n\n  To begin you must specify the LM's initial altitude \n  and fuel level. To simulate the actual LM use \n  values of 1300 meters and 500 liters, respectively.\n\n  Good luck and may the force be with you!")

#showWelcome()

def getFuel():
   fuel = eval(input("Enter the initial amount of fuel on board the LM (in liters): "))
   if fuel > 0:
      return fuel
   elif fuel <= 0:
      print("Error! Please enter a positive number.")
#getFuel()

def getAltitude():
   altitude = eval(input("Enter the initial altitude of the LM (in meters): "))
   if altitude in range(1,10000):
      return altitude
   else:
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")

#getAltitude()


def getFuelRate(currentFuel):
   x = eval(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))

   if x >= 0 and x <= 9:
      return min(x, currentFuel)
   elif x < 0 or x > 9:
      print("ERROR: Fuel rate muse be between 0 and 9, inclusive")
      return getFuelRate(currentFuel)
      
   
def updateAcceleration(gravity, fuelRate):
   acceleration = gravity * ((fuelRate/5) - 1)
   return acceleration
 
	
def updateAltitude(altitude, velocity, acceleration):
   altitude = altitude + velocity + (acceleration / 2)
   return altitude

def updateVelocity(velocity, acceleration):
   velocity = velocity + acceleration
   return velocity

def updateFuel(fuel, fuelRate):
   fuel = fuel - fuelRate
   return fuel

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):

   print("Elapsed Time:", elapsedTime, "s")
   print("Fuel:", fuelAmount, "l")
   print("Rate:", fuelRate, "l/s")
   print("Altitude:", "{0:.2f}".format(round(altitude, 2)), "m")
   print("Velocity:", "{0:.2f}".format(round(velocity, 2)), "m/s")


def displayLMLandingStatus(velocity):
   if velocity >= -1 and velocity <= 0:
      print("Status at landing - The eagle has landed!")
   elif velocity > -10 and velocity < -1:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   elif velocity <= -10:
      print("Status at landing - Ouch - that hurt!")
