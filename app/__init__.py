import tkinter as tk

def convert():
    input_value = float(input_entry.get())
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()
    
    
    conversion_rates = {
        ("Miles", "Kilometer"): 1.60934,
        ("Kilometer", "Miles"): 0.621371,
        ("Pounds", "Kilograms"): 0.453592,
        ("Kilogrmas", "Pounds"): 2.20462,
        ("Inches", "Centimeters"): 2.54,
        ("Centimeters", "Inches"): 0.394
    }
    
    result = input_value * conversion_rates[]