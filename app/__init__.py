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