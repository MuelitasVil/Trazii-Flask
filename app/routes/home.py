from flask import flash, Blueprint, render_template, request, redirect, url_for
from app.shared.localStorage import localStorage
from app.services.auth.authentication import Login  

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

@home.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        
        user = request.form["correo"]
        clave = request.form["clave"]

        data = {
            'telefono': str(user),
            'clave': str(clave)
        }

        if Login(data):
            storage = localStorage()
            subjectData = storage.get_subject_data()
            return redirect(url_for("menu.Menu"))
    
        else:
            flash('Por favor revisa tus datos:\nTu número de celular o contraseña son incorrectos')

        return redirect(url_for("home.index"))
    
    else:
        return render_template('home.html')
    