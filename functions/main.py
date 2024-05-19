# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app, credentials, storage, firestore

import json
import csv
from flask import jsonify
from datetime import datetime

initialize_app()
db = firestore.client()


#
@https_fn.on_request()
def on_request_example(req: https_fn.Request) -> https_fn.Response:    
    
    bucket_name = 'uab-the-hack.appspot.com'
    file_name = 'municipis_totals.csv'
    try:
        # Download the file from Firebase Storage
        firebase_storage = storage.bucket(bucket_name)
        blob = firebase_storage.blob(file_name)
        blob.download_to_filename('/tmp/' + file_name)  # Download to temporary location

        # Return the file content (in a real case, you might store this somewhere or process it)
        with open("/tmp/" + file_name, encoding = "latin-1") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            json_array = list()
            i = 0
            for row in csv_reader:
                if i == 0:
                    json_names = row
                    i += 1
                else:
                    json_array.append(row)




        json_array = sorted(json_array, key=lambda x: x[6])
        json_array = sorted(json_array,key=lambda x: x[2])
        json_array = sorted(json_array,key=lambda x: x[1])
        json_array = sorted(json_array,key=lambda x: x[0])

        array_sortida = [ dict(itinerari1=[], itinerari2=[], itinerari3=[], itinerari4=[]) for i in range(4)]

        counter = 1


        # Inicialitzem data al primer dilluns de Juny 2024
        mes = 6
        contador_dia = 3
        contador_setmana = 1

        hores = [8,8,8,8]
        minuts = [0,0,0,0]

        temps_total = 0

        for row in json_array:
            data_dia = datetime(2024, mes, contador_dia, 8, 0, 0, 0)

            if row[6] == "30 MINUTOS":
                temps = 30
            else:
                temps = 60    

            temps_total += temps

            duracio = temps // 10
            
            hores_visita = []
            for i in range(10):
                inici = datetime(2024, mes, contador_dia, hores[counter-1], minuts[counter-1], 0, 0)
                minuts[counter-1] += duracio
                if minuts[counter-1] >= 60:
                    hores[counter-1] += 1
                    minuts[counter-1] = 0
                
                final = datetime(2024, mes, contador_dia, hores[counter-1], minuts[counter-1], 0, 0)
                hores_visita.append({ "start":inici, "end":final})

            punt_actual = dict(comarca=row[2], municipi=row[4], temps_estimat = temps, hores = hores_visita) 

            dia = dict(data=data_dia, pd = punt_actual)
            match counter:
                case 1:  
                    array_sortida[int(row[1])-1]["itinerari1"].append(dia)
                    counter += 1
                case 2:
                    array_sortida[int(row[1])-1]["itinerari2"].append(dia)
                    counter += 1
                case 3:
                    array_sortida[int(row[1])-1]["itinerari3"].append(dia)
                    counter += 1
                case 4:
                    array_sortida[int(row[1])-1]["itinerari4"].append(dia)
                    counter = 1

            
            if temps_total >= 1200:
                if contador_setmana > 4:
                    contador_setmana = 1
                    contador_dia += 3
                else:
                    contador_setmana += 1
                    contador_dia += 1
                if contador_dia > 30:
                    contador_dia = 1
                    mes += 1
                temps_total =0
                hores = [8,8,8,8]
                minuts = [0,0,0,0]

        doc_ref = db.collection('routes').add({"Blocs":array_sortida})

        return {
            'file_name': file_name,
            'Status': "Success"
        }, 200
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500       


