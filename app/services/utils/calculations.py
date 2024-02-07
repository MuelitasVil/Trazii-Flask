def getTotalArea(Information_Fincas):
    area = 0
    for key in Information_Fincas:
        Finca = Information_Fincas[key]
        if 'FIAR' not in Finca:
            return 0
        if ',' in Finca['FIAR']:
            area += float(Finca['FIAR'].replace(',', '.'))
        else:
             area += int(Finca['FIAR'])
    return area

def getTotalPeso(Information_Bovinos):
    peso = 0
    for key in Information_Bovinos:
        bovino = Information_Bovinos[key]
        