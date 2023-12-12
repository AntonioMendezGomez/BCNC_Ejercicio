from flask import Flask, jsonify, request

Update_Users_All = Flask(__name__)

# Datos de ejemplo (puedes reemplazar esto con una base de datos real)
usuarios = [
    {"id": 1, "nombre": "Usuario1", "correo": "usuario1@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    {"id": 2, "nombre": "Usuario2", "correo": "usuario2@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    # Agrega más usuarios según sea necesario
]

# Ruta para obtener todos los usuarios
@Update_Users_All.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

# Ruta para actualizar completamente un usuario por ID
@Update_Users_All.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)

    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    # Actualizar completamente el usuario con los datos proporcionados
    datos_actualizados = request.json
    usuario.update(datos_actualizados)

    return jsonify({"mensaje": "Usuario actualizado completamente", "usuario": usuario})

if __name__ == '__main__':
    Update_Users_All.run(debug=True)


#Se ha agregado una nueva ruta (/api/usuarios/<int:usuario_id>) con el método PUT para actualizar completamente un usuario por su ID.