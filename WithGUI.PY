import tkinter as tk
from tkinter import ttk
from datetime import datetime

def calculate_fare():
    destination = destination_var.get()
    passenger_type = passenger_type_var.get()

    if destination in fares:
        price = fares[destination]
        distance = kilometers[destination]

        fare_output = f"FARE: {price} PHP\n"
        
        if passenger_type in discounted:
            discount = price * 0.20
            discounted_price = price - discount
            fare_output += f"Discounted Fare ({passenger_type}): {discounted_price} PHP\n"
        else:
            discounted_price = price

        fare_output += f"Distance: {distance} KM"
        output_label.config(text=fare_output)
    else:
        output_label.config(text="Invalid Destination")


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

discounted = {"PWD", "Senior", "Student"}


root = tk.Tk()
root.title("Saulog Transit Fare Calculator")


tk.Label(root, text="Destination To:").grid(row=0, column=0, pady=5, sticky=tk.W)
destination_var = tk.StringVar()
destination_combobox = ttk.Combobox(root, textvariable=destination_var, values=list(fares.keys()), state="readonly")
destination_combobox.grid(row=0, column=1, pady=5)
destination_combobox.set("Select Destination")

tk.Label(root, text="Passenger Type:").grid(row=1, column=0, pady=5, sticky=tk.W)
passenger_type_var = tk.StringVar()
passenger_type_combobox = ttk.Combobox(root, textvariable=passenger_type_var, values=["None", "PWD", "Senior", "Student"], state="readonly")
passenger_type_combobox.grid(row=1, column=1, pady=5)
passenger_type_combobox.set("None")


calculate_button = tk.Button(root, text="Calculate Fare", command=calculate_fare)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

output_label = tk.Label(root, text="", justify=tk.LEFT)
output_label.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()
