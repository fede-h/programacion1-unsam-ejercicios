import datetime

def vida_en_segundos(fecha_nac):
    '''Toma una fecha en formato 'dd/mm/AAAA' y devuelve
    la cantidad de segundos transcurridos hasta hoy'''

    fecha_nac = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
    diferencia = datetime.datetime.now() - fecha_nac

    return diferencia.total_seconds()

def primavera():
    '''Devuelve la cantidad de días que faltan
    para la próxima primavera'''

    if datetime.date.today() < datetime.date(datetime.date.today().year, 9, 21):
        proxima_primavera = datetime.date(datetime.date.today().year, 9, 21)
    else:
        proxima_primavera = datetime.date(datetime.date.today().year + 1, 9, 21)

    diferencia = proxima_primavera - datetime.date.today()
    
    return diferencia.days

def dias_habiles(inicio, fin, feriados):
    '''
    Calcula los dias hábiles
    entre dos fechas dadas: inicio, fin y una lista
    de feriados en el medio de esas dos fechas
    Formato de las fechas: dd/mm/AAAA 
    '''
    inicio = (datetime.datetime.strptime(inicio, '%d/%m/%Y'))
    inicio = datetime.date(inicio.year, inicio.month, inicio.day)
    fin = (datetime.datetime.strptime(fin, '%d/%m/%Y'))
    fin = datetime.date(fin.year, fin.month, fin.day)
    dias_habiles = 0
    feriados = [datetime.datetime.strptime(fecha, '%d/%m/%Y') for fecha in feriados]
    feriados = [datetime.date(fecha.year, fecha.month, fecha.day) 
        for fecha in feriados if fecha.weekday() < 5]
    
    for i in range((fin - inicio).days):
        fecha = inicio + datetime.timedelta(days = i)
        if fecha.weekday() < 5:
            dias_habiles += 1

    return dias_habiles-len(feriados)
