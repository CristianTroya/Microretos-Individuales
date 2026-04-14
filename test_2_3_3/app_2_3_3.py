# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    # Buscamos el archivo 'index.html' dentro de la carpeta /templates
    # También podemos pasar datos como variables (nombre="Ana")
    return render_template("index_2_3_3.html", nombre="Ana")

if __name__ == "__main__":
    app.run(debug=True)