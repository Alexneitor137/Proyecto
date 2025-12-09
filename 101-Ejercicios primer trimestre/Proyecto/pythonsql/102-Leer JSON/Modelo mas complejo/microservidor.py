#Importo flask para poder crear webs
from flask import Flask, render_template

#Creo una nueva aplicacion
app = Flask(__name__)

#Escucho en la ruta raiz
@app.route("/")
def inicio():
    #Y renderizo una plantilla llamada index.html
    return render_template("index.html")

#Si este archivo no es una libreria y es el archivo principal
if __name__ == "__main__":
    #Poner en marcha la aplicacion
    app.run(debug=True)