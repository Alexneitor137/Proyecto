from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def inicio():
  mi_nombre = "Alejandro"
  return render_template("variable.html",nombre = mi_nombre)

if __name__ == "__main__":
  app.run(debug=True)