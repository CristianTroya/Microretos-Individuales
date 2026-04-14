# Importamos la función para manejar plantillas
#Mi ip 185.197.91.157
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    # Buscamos el archivo 'perfil_2_3_1.html' dentro de la carpeta /templates
    # También podemos pasar datos como variables (nombre="Cristian")
    return render_template("perfil_2_3_2.html", nombre="Cristian", estudiante="Cristian Troya Moreno", nickname="Cris", id_dev="2296")
if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)