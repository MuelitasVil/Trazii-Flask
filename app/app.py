from flask import Flask, render_template, request, redirect, url_for
from app.routes.home import home
from app.routes.menu import menu
from app.routes.cargas import cargas
from app.shared.localStorage import localStorage

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/uploads"
app.secret_key = 'th3r4n0ms1ng'

app.register_blueprint(home)
app.register_blueprint(menu)
app.register_blueprint(cargas)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
