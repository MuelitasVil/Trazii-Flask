from flask import Blueprint, render_template, request, abort
from datetime import datetime
from werkzeug.utils import secure_filename

from app.services.excel.excelManager import ExcelManager
from app.shared.localStorage import localStorage

cargas = Blueprint("cargas", __name__, static_folder="static", template_folder="templates")

@cargas.route('/CargasMasivas', methods = ["POST", "GET"])
def Cargas():
    storage = localStorage()
    
    nowTime = datetime.utcnow()
    expirationTime = datetime.fromtimestamp(int(storage.get_exp()))

    if nowTime > expirationTime: 
        return render_template("cargas.html")

    return abort(404)

@cargas.route('/upload', methods = ["POST"])
def upload():
    file = request.files['uploadFile']
    
    if not file:
        return "NO ARCHIVO"
     
    fileName = secure_filename(file.filename)

    if file and VerifyExel(fileName):
        print(fileName)
        excel = ExcelManager(file)
        excel.ExcelUpdateToDB()
        return "Exel"
    else:
        return "NO EXEL" 
        

def VerifyExel(fileName):
    if fileName.endswith(".xlsm") or fileName.endswith(".xlsb") or fileName.endswith(".xlsx"):
        return True
    return False
