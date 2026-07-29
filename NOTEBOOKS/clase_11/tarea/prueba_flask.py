from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return "¡Bienvenido a la API en Flask!"

@app.route('/api/estado')
def estado_servidor():
    # Retorna una respuesta JSON
    return jsonify({"servidor": "Activo", "latencia_ms": 15})

if __name__ == '__main__':
    app.run(debug=True)