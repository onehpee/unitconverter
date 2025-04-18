from flask import Flask, render_template, request, redirect, url_for, session
import secrets

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gunit'
    
    from .views import views
    from .auth import auth
    
    def converter_unit(units, value, unit_from, unit_to):
        # same unit
        if unit_from == unit_to:
            return value
        # converter to refer_unit
        refer_unit = float(value) * units[unit_from]

        # converter to desired
        return refer_unit / units[unit_to]
    
    def convert_temp(value, unit_from, unit_to):
        value = float(value)
        if unit_from == unit_to:
            return value

        #original unit to Celsius
        if unit_from == "c":
            value_in_celsius = value
        elif unit_from == "f":
            value_in_celsius = (value - 32) * 5 / 9
        else:
            value_in_celsius = value - 273.15

        #Celsius to the target unit
        if unit_to == "c":
            return value_in_celsius
        elif unit_to == "f":
            return (value_in_celsius * 9 / 5) + 32
        else:
            return value_in_celsius + 273.15

    
    def length():
    # key unit value in meter
        LENGTH = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344,
    }
        

    
    app.register_blueprint(views, url_prefix='/' )
    app.register_blueprint(auth, url_prefix='/' )
    
    return app