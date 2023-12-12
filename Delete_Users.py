from flask import Flask, jsonify, request

Delete_Users = Flask(__name__)

# Datos de ejemplo
usuarios = [
    {
        "id": 1,
        "nombre": "Usuario1",
        "correo": "usuario1@example.com",
        "Fechanacimiento": "XXXX-XX-XX",
        "viviendas": [
            {"id": 101, "direccion": "Calle 1", "ciudad": "Ciudad A", "pais": "Pais X"},
            {"id": 102, "direccion": "Calle 2", "ciudad": "Ciudad B", "pais": "Pais Y"},
        ],
    },
    {
        "id": 2,
        "nombre": "Usuario2",
        "correo": "usuario2@example.com",
        "Fechanacimiento": "XXXX-XX-XX",
        "viviendas": [
            {"id": 201, "direccion": "Calle 3", "ciudad": "Ciudad A", "pais": "Pais X"},
            {"id": 202, "direccion": "Calle 4", "ciudad": "Ciudad C", "pais": "Pais Z"},
        ],
    },
    # Agrega más usuarios según sea necesario
]

# Ruta para obtener todos los usuarios
@Delete_Users.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

# Ruta para borrar un usuario por ID
@Delete_Users.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def borrar_usuario(usuario_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)

    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    if usuario.get("viviendas"):
        return jsonify({"mensaje": "No se puede borrar el usuario, tiene viviendas asociadas"}), 400

    usuarios.remove(usuario)

    return jsonify({"mensaje": "Usuario borrado exitosamente"})

if __name__ == '__main__':
    Delete_Users.run(debug=True)

#Se ha agregado una ruta /api/usuarios/<int:usuario_id> con el método DELETE para borrar un usuario por su ID. Antes de borrar el usuario, se verifica si tiene viviendas asociadas. Si tiene viviendas, se devuelve un mensaje de error; de lo contrario, se procede a borrar el usuario.