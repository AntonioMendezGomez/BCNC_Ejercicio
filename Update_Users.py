from flask import Flask, jsonify, request

Update_Users = Flask(__name__)

# Datos de ejemplo
usuarios = [
    {"id": 1, "nombre": "Usuario1", "correo": "usuario1@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    {"id": 2, "nombre": "Usuario2", "correo": "usuario2@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    # Agrega más usuarios según sea necesario
]

# Ruta para obtener todos los usuarios
@Update_Users.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

# Ruta para actualizar parcialmente un usuario por ID
@Update_Users.route('/api/usuarios/<int:usuario_id>', methods=['PATCH'])
def actualizar_usuario(usuario_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)

    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    # Actualizar campos proporcionados en la solicitud
    campos_actualizados = request.json
    for campo, valor in campos_actualizados.items():
        if campo in usuario:
            usuario[campo] = valor

    return jsonify({"mensaje": "Usuario actualizado parcialmente", "usuario": usuario})

if __name__ == '__main__':
    Update_Users.run(debug=True)

#Se ha agregado una nueva ruta (/api/usuarios/<int:usuario_id>) con el método PATCH para actualizar parcialmente un usuario por su ID.