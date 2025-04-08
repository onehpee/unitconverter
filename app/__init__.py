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

    
    app.register_blueprint(views, url_prefix='/' )
    app.register_blueprint(auth, url_prefix='/' )
    
    return app