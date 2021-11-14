import pandas as pd
import csv

mainpath = "E:\\Git\\Github\\9.- Data Science\\appDSpy\\datasets"
filename = "\\titanic\\titanic3.xls"

#como segundo parametro pasar el nombre de la hoja excel
titanicExcel = pd.read_excel(mainpath + "\\" + filename,"titanic3")

# Ejemplos de conversion
titanicExcel.to_csv(mainpath + "\\titanic\\titanic_harry.csv")
titanicExcel.to_excel(mainpath + "\\titanic\\titanic_harry.xls")
titanicExcel.to_json(mainpath + "\\titanic\\titanic_harry.json")