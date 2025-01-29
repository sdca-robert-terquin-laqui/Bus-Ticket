import datetime
import tkinter as tk
from tkinter import ttk

destination = input("Enter Destination To: ")
vehicleNumber = input("Enter Bus Number: ")
driverName = input("Enter Driver Name: ")
conductorName = input("Enter Conductor Name: ")
passengerType = input("For Discounts (PWD, Senior, Student): ")


print("\nSaulog Transit (PITX - Ternate, Cavite)")

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")


print(f"Date: {date}")
print(f"Time: {time}")
print(f"Driver: {driverName}")
print(f"Conductor: {conductorName}")
print(f"Bus Number: {vehicleNumber}")
print(f"Ride: PITX - {destination}")

fares = {
    "Bacoor": 40,
    "Kawit": 45,
    "General Trias": 60,
    "Tanza": 80,
    "Naic": 100,
    "Maragondon": 115,
    "Ternate": 125,
    
}

kilometers = {
    
    "Bacoor": 14,
    "Kawit": 17,
    "General Trias": 18,
    "Tanza": 24,
    "Naic": 32,
    "Maragondon": 40,
    "Ternate": 47,

}

discounted = {

    "PWD",
    "Senior",
    "Student",

}

if destination in fares:
    price = fares[destination]
    print(f"FARE: {price} "+ "php")

if passengerType in discounted:
        less = price * 0.20
        newPrice = price - less
        print(f"Discounted Fare ({passengerType}) : {newPrice} ")

if destination in kilometers:
    distance = kilometers[destination]
    print(f"Distance: {distance} "  + "KM")



print("Wherever you are, we are there......")