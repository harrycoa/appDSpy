import pandas as pd
import csv
# Leer CSV desde url
import urllib3

medals_url = "http://winterolympicsmedals.com/medals.csv"
medals_data = pd.read_csv(medals_url)
medals_data.head()

# Leer CSV desde url con urllib3
http = urllib3.PoolManager()
r = http.request('GET', medals_url)
r.status
# Asignamos la respuesta a una variable
response = r.data

# el objeto response contiene un string binario, asi que lo convertimos a un string decodificando a utf-8
str_data = response.decode('utf-8')

# Dividimos el string en un array de filas, separado por enters
lines = str_data.split("\n")

# La primera linea contiene la cabecera, asi que la extraemos
