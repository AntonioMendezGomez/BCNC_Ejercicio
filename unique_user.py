from flask import Flask, jsonify

unique_user = Flask(__name__)

# Datos de ejemplo
usuarios = [
    {"id": 1, "nombre": "Usuario1", "correo": "usuario1@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    {"id": 2, "nombre": "Usuario2", "correo": "usuario2@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    # Agrega más usuarios según sea necesario
]

# Ruta para obtener un usuario por ID
@unique_user.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)
    
    if usuario:
        return jsonify({"usuario": usuario})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    unique_user.run(debug=True)



#En este caso se ha modificado la ruta a /api/usuarios/<int:usuario_id>, donde <int:usuario_id> es una parte dinámica de la URL que se espera que sea un entero (ID del usuario). La función obtener_usuario busca un usuario con el ID proporcionado y responde con los detalles del usuario si se encuentra o un mensaje de error si no se encuentra.
