from flask import Flask, render_template,request

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('length.html')


def length():
    if request.method == 'POST':
        try:
            length = float(request.form["len"])
            unit_from = request.form["unit_from"]
            unit_to = request.form["unit_to"]
            conversion_factors = {
                'cm': 1,
                'm': 100,
                'km': 100000,
                'in': 2.54,
                'ft': 30.48,
                'yd': 91.44,
                'mi': 160934
             }
            if unit_from in conversion_factors and unit_to in conversion_factors:
                converted = length * (conversion_factors[unit_from] / conversion_factors[unit_to])
            else:
                error = "Invalid unit conversion."
                return render_template('result.html', error=error)
        except ValueError:
            error= "Invalid input. Please enter a valid number."
            return render_template('result.html', error=error)
        
        return render_template('result.html', converted=converted, unit_to=unit_to)
    return render_template('length.html')
