import datetime
import os
import requests

def abrir_aula(algebra_link, db_link, db_activity):
    dia_semana = datetime.date.today()
    dia_semana = dia_semana.weekday()

    if dia_semana == 0:
        link = 'https://meet.google.com/dxw-wpus-weo?authuser=1'
        os.system(f'start {link}')

    elif dia_semana == 1:
        link = 'https://meet.google.com/hia-cbcf-emz'
        os.system(f'start {link}')

    elif dia_semana == 2:
        link = db_link
        os.system(f'start {link}')
        os.system(f'start {db_activity}')

    elif dia_semana == 3:
        link = 'https://meet.google.com/dwb-jdom-cec?authuser=1'
        os.system(f'start {link}')

    elif dia_semana == 4:
        link = algebra_link
        os.system(f'start {link}')

    else:
        print('Hoje é fim de semana,descansa ai po!')

    os.system("pause")
