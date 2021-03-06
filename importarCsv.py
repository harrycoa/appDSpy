import pandas as pd
import csv
import urllib3
## DATA 1
data = pd.read_csv("E:\\Git\\Github\\9.- Data Science\\appDSpy\\datasets\\titanic3.csv")
data.head()

# Otra forma de llamar
mainpath = "E:\\Git\\Github\\9.- Data Science\\appDSpy\\datasets"
filename = "ejemplotxt.txt"
fullpath = mainpath + "\\" + filename

### DATA 2
data2 = pd.read_csv(fullpath)
data2.head()
data2.columns.values
data_cols = pd.read_csv(mainpath + "\\" + "columnas.csv" )
data_col_list = data_cols["Column_Names"].tolist()
# mostrar columnas data_col_list
# agregamos el archivo modelo y juntamos el archivo de columnas
data2 = pd.read_csv(mainpath + "\\" + "modelo.csv",
                   header = None, names = data_col_list)
data2.columns.values
data_col_list


### DATA 3
# Carga de datos a travez de la funcion open
data3 = open(mainpath + "\\" + "modelo.txt", "r")
# extraer la data linea a linea

# metodo strip.- dividir y eliminar los espacios en blanco que sobra inicio o final
# metodo split.- divide la linea de texto por un delimitador o espacio
# metodo readline.- leer una linea
cols = data3.readline().strip().split(",")
n_cols = len(cols)
n_cols

# con contador
contador = 0
main_dict = {}
for col in cols:
    main_dict[col] = []

main_dict

# rellenar el array vacio con la data
for line in data3:
    values = line.strip().split(",")
    for i in range(len(cols)):
        main_dict[cols[i]].append(values[i])
    contador +=1
print ("El data set tiene %d filas y %d columnas" % (contador, n_cols))
print ("El data set tiene %d filas y %d columnas" % (contador, n_cols))

df3 = pd.DataFrame(main_dict)
df3.head()

## Lectura y Escritura de archivos
infile = mainpath + "\\" + "customer\\Customer Churn Model.txt"
outfile = mainpath + "\\" + "customer\\Tab Customer Churn Model.txt"

with open(infile, "r") as infile1:
    with open(outfile, "w") as outfile1:
        for line in infile1:
            fields = line.strip().split(",")
            outfile1.write("\t".join(fields))
            outfile1.write("\n")

df4 = pd.read_csv(outfile, sep = "\t")
df4.head()

## Leer CSV desde url
medals_url = "http://winterolympicsmedals.com/medals.csv"
medals_data = pd.read_csv(medals_url)
medals_data.head()

## Leer CSV desde url con urllib3

http = urllib3.PoolManager()
r = http.request('GET', medals_url)
r.status
response = r.data


## Utilizamos csv lib
cr = csv.reader(response)

for row in cr:
    print(row)