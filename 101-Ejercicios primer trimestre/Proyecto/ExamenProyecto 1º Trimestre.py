import mysql.connector
from flask import Flask

conexion = mysql.connector.connect(
  host="localhost",
  user="Manolo",
  password="Portafolio123$",
  database="portafolioexamen"
)
cursor = conexion.cursor()
app = Flask(__name__)

@app.route("/")
def holamundo():
    cursor.execute("SELECT * FROM vista_piezas;")
    filas = cursor.fetchall()

    cadena = ''' 
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portafolio Examen</title>
        <link rel="stylesheet" href="style.css">
        <style>
            html {
                color: black;
                background-color: aqua;
                font-family: Georgia, 'Times New Roman', Times, serif;
                text-align: center;
            }       
            body {
                width: 800px;
                background: white;
                margin: auto;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }

            #contenedorportafolio {
                display: grid;
                grid-template-columns: repeat(3, 1fr);  /* Tres columnas flexibles */
                gap: 10px;  /* Espaciado entre los elementos */
                padding: 20px;
            }

            article {
                background-color: #000;
                color: white;
                padding: 10px;
                text-align: center;
                border-radius: 10px;
            }

            article h3 {
                font-size: 1.5em;
                font-weight: bold;
            }

            article img {
                max-width: 100%;
                height: auto;
                border-radius: 5px;
            }

            header {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin: auto;
                padding: 20px;
            }

            h1 {
                text-align: center;
            }

        </style>
    </head>
    <body>
        <header>
            <h1>Portafolio de Alejandrus Calderonus Sanchicus</h1>
        </header>
        <main>
            <div id="contenedorportafolio">'''

    # Generación de artículos dentro del contenedor del grid
    for fila in filas:
        cadena += f'''
        <article>
            <p>{fila[0]}</p>
            <h3>{fila[1]}</h3>
            <p>{fila[2]}</p>
            <img src="{fila[3]}" alt="Imagen de {fila[1]}">
        </article>
        '''

    cadena += '''  
            </div>
        </main>
    </body>
    </html>
    '''

    return cadena

if __name__ == "__main__":
    app.run(debug=True)
