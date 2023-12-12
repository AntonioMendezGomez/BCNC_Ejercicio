from flask import Flask, jsonify

Api_users = Flask(__name__)

# Datos de ejemplo
usuarios = [
    {"id": 1, "nombre": "Usuario1", "correo": "usuario1@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    {"id": 2, "nombre": "Usuario2", "correo": "usuario2@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    # Agrega más usuarios según sea necesario
]

# Ruta para obtener todos los usuarios
@Api_users.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == '__main__':
    Api_users.run(debug=True)


#Al ingresar esa URL en tu navegador o al hacer una solicitud GET utilizando herramientas como curl o Postman,obtendrás una respuesta JSON con todos los usuarios.