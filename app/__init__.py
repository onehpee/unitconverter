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
        units = LENGTH.keys()

        # Prev post is none if result copy and delete in session
        result = session.pop("result", None)

        if request.method == "POST":
            value = request.form.get("length")
            unit_from = request.form.get("unit_from")
            unit_to = request.form.get("unit_to")

            # check post values
            if (
                (not value or value.isalpha())
                or unit_from not in units
                or unit_to not in units
            ):
                return redirect(url_for("length"))

            result = converter_unit(
                units=LENGTH, value=value, unit_from=unit_from, unit_to=unit_to
            )
            view_result = f"{value}{unit_from} = {result}{unit_to}"
            # add result
            session["result"] = view_result
            return redirect(url_for("length"))

        return render_template("./pages/length.html", units=units, result=result)
def weight():
    # value in grams
    WEIGHT = {
        "mg": 0.001,
        "gr": 1,
        "kg": 1000,
        "ounce": 28.35,
        "pound": 453.59,
    }       

    
    app.register_blueprint(views, url_prefix='/' )
    app.register_blueprint(auth, url_prefix='/' )
    
    return app