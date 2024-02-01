from flask import flash ,Blueprint, render_template 

# import pandas as pd
# import json
# import plotly
# import plotly.express as px

from app.services.sync.sincronizar import sincronizar_datos
from app.services.utils.calculations import getTotalArea
from app.shared.localStorage import localStorage

menu = Blueprint("menu", __name__, static_folder="static", template_folder="templates")

@menu.route('/Menu', methods = ["POST", "GET"])
def Menu():
    
    sincronizar_datos()
    storage = localStorage()
    
    # Informaacion usuario
    user_information = storage.get_subject_data()

    # Trazables 
    fincas = storage.get_Fincas()
    bovinos = storage.get_Bovinos()

    # Cantidad de trazables (Informacion sacada de datos) 
    cantidades = storage.get_Cantidades()

    # Trazas
    compras = storage.get_Compra()
    ordeño = storage.get_Ordeño()

    # Datos  
    cantidad_Bovinos = cantidades['Cant_BOV']
    cantidad_Colaboradores = cantidades['Cant_COL']
    area_Total = getTotalArea(fincas)

    # Informacion fincas
    headingsFincas = ("Finca", "Bovinos", "Area", "Colaboradores")
    dataFincas  = getTablaFincas(fincas)
    
    # Informacion compras 
    # headingsCompras = ("Cantidad Animales", "Peso Comprado", "Gasto Total")
    # dataCompras = getTablaCompras(compras)

    # Informacion de Eficiencia 
    headingsProduccion = ["Produccion"]
    hadingsReproduccion = ["Reproduccion"]
    headingsPastoreo = ["Pastoreo"]
    
    dataordeño = getTablaOrdeño(ordeño)

    dataProduccion = [
        ["Litros / ha : {}".format(getLitrosH(dataordeño, area_Total))],
        ["Litros vaca / dia : {}".format(dataordeño[1])],
        ["Kg / ha : NONE"],
        ["Kg / animal : NONE"]
         
    ]
    
    dataReproduccion = [
        ["Dias abiertos : NONE"],
        ["Servicios / preñez : NONE"],
    ] 
    
    dataPastoreo = [
        ["Dias de rotacion : NONE"],
        ["UGG : NONE"],
        ["kgMS / ha : NONE"]
    ]

    dataEficiencia = [
        (headingsProduccion, dataProduccion),
        (hadingsReproduccion, dataReproduccion),
        (headingsPastoreo, dataPastoreo)
    ]


    # Students data available in a list of list
    # students = [['Akash', 34, 'Sydney', 'Australia'],
    #            ['Rithika', 30, 'Coimbatore', 'India'],
    #            ['Priya', 31, 'Coimbatore', 'India'],
    #            ['Sandy', 32, 'Tokyo', 'Japan'],
    #            ['Praneeth', 16, 'New York', 'US'],
    #            ['Praveen', 17, 'Toronto', 'Canada']]
     
    # Convert list to dataframe and assign column values
    # df = pd.DataFrame(students,
    #                  columns=['Name', 'Age', 'City', 'Country'],
    #                  index=['a', 'b', 'c', 'd', 'e', 'f'])
     
    # Create Bar chart
    # fig = px.bar(df, x='Name', y='Age', color='City', barmode='group')
     
    # Create graphJSON
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) 
    
    #return render_template('grafico.html', graphJSON=graphJSON)
    
    #print(user_information)

    return render_template(
        "menu.html",
        NombreAdministrador = user_information['nombre'],
        CantidadBovinos = cantidad_Bovinos,
        AreaTotal = area_Total,
        CantidadColaboradores = cantidad_Colaboradores,
        headingsFincas = headingsFincas,
        dataFincas = dataFincas,
        # headingsCompras = headingsCompras,
        # dataCompras = dataCompras,
        dataEficiencia = dataEficiencia
    )

def getLitrosH(dataordeño, area_Total):
    if area_Total == 0:
        return 0
    return round(dataordeño[0] / area_Total, 2)

def getTablaFincas(fincas):
    data = []
    for key in fincas:

        finca = fincas[key]
        nombre = finca['FINA']

        if 'Cantidad_BOV' not in finca:
            bovinos = 0
        else:
            bovinos = finca['Cantidad_BOV']

        area = finca['FIAR']

        if 'Cantidad_COL' not in finca:
            colaboradores = 0
        else:
            colaboradores = finca['Cantidad_COL']

        data.append([nombre,bovinos,area,colaboradores])
    
    return data

def getTablaCompras(compras):
    data = []
    pesoTotal = 0
    valorTotal = 0
    cantidadTotal = 0

    for key in compras:
        compra = compras[key]
        lote = False

        if 'COCA' in compra: 
            cantidad = compra['COCA']
            lote = True
        else:
            cantidad = 1
        
        if 'COPE' in compra:
            if lote:
                peso = float(compra['COPE']) * cantidad
            else:
                peso = float(compra['COPE'])

        if 'COVA' in compra:
            if lote: 
                valor = float(compra['COVA']) * cantidad
            else: 
                valor = float(compra['COVA'])

        pesoTotal += peso
        valorTotal += valor
        cantidadTotal += cantidad

    data.append([cantidadTotal, pesoTotal, valorTotal])
    return data

def getTablaOrdeño(ordeños):
    data = []
    lecheTotal = 0

    for key in ordeños:

        ordeño = ordeños[key]

        if 'LECA' in ordeño: 
            cantidad = float(ordeño['LECA'])
        else:
            cantidad = 0
        
        lecheTotal += cantidad
    
    lecheDia = lecheTotal / 30

    return [lecheTotal, round(lecheDia,2)]
