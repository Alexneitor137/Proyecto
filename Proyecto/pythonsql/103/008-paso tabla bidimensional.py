from flask import Flask, render_template 
import mysql.connector                    # Importamos MySQL
###################### MYSQL ##############################################
conexion = mysql.connector.connect(
    host="localhost",
    user="Manolo",
    password="Portafolio123$",
    database="portafolioexamen"
)                                       # Datos de conexión a la base de datos
cursor = conexion.cursor()                # Creo un cursor MySQL
#------------Esto envia las tablas----------------
cursor.execute("SHOW TABLES;")            # Muestra las tablas de la base de datos
tablas = []                               # Creo una lista vacia
filas = cursor.fetchall()                 # Lo guardo en una lista
for fila in filas:                        # Recorro el resultado
  tablas.append(fila[0])                  # Lo añado a la lista de tablas   
  #-----Esto envia las cabeceras de las tablas---------- 
cursor.execute("SHOW COLUMNS in piezasportafolio;")            # Muestra las columnas de una tabla de la base de datos
columnas = []                               # Creo una lista vacia
filas = cursor.fetchall()                 # Lo guardo en una lista
for fila in filas:                        # Recorro el resultado
  columnas.append(fila[0])                  # Lo añado a la lista de tablas    
#---------------Esto envia toda la tabla--------------------------------
cursor.execute("SELECT * FROM piezasportafolio;")     
contenido_tabla = cursor.fetchall()      
###################### MYSQL ##############################################

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template(
    "backoffice.html",
    mis_tablas = tablas,
    mis_columnas = columnas,
    mi_contenido_tabla = contenido_tabla
    ) 
  
if __name__ == "__main__":
  app.run(debug=True)