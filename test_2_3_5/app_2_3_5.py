import sqlite3
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/debug")
def ver_coleccion():
    # 1. Conectamos con el archivo de la base de datos (ruta relativa al archivo)
    db_path = Path(__file__).parent / "reto_cristian.db"
    conexion = sqlite3.connect(str(db_path))
    
    # 2. Configuramos la conexión para que devuelva diccionarios (más fácil para Jinja2)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    
    # 3. Ejecutamos la consulta SQL
    cursor.execute("SELECT * FROM LOGS")
    
    # 4. Guardamos todos los resultados en una variable
    datos = cursor.fetchall()
    
    # 5. Cerramos la conexión
    conexion.close()
    
    # 6. Enviamos los datos reales a la plantilla
    return render_template("lista_2_3_5.html", items=datos)

if __name__ == "__main__":
    app.run(debug=True)