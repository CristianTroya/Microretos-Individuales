from flask import Flask, render_template

app = Flask(__name__)

@app.route("/coleccion")
def ver_coleccion():
    # Creamos una lista de diccionarios con datos de prueba
    mis_favoritos = [
        {"id": "Spider-Man 2", "descripcion": "Película de superhéroes"},
        {"id": "Indiana Jones", "descripcion": "Película de aventuras"},
        {"id": "Interstellar", "descripcion": "Película de ciencia ficción"}
    ]
    # Enviamos la lista completa a la plantilla con el nombre 'favoritos'
    return render_template("lista_2_3_4.html", favoritos=mis_favoritos)

if __name__ == "__main__":
    app.run(debug=True)
