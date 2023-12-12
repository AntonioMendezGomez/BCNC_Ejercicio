from flask import Flask, jsonify

Users_Houses = Flask(__name__)

# Datos de ejemplo
usuarios = [
    {
        "id": 1,
        "nombre": "Usuario1",
        "correo": "usuario1@example.com",
        "Fechanacimiento": "XXXX-XX-XX",
        "viviendas": [
            {"id": 101, "direccion": "Calle 1"},
            {"id": 102, "direccion": "Calle 2"},
        ],
    },
    {
        "id": 2,
        "nombre": "Usuario2",
        "correo": "usuario2@example.com",
        "Fechanacimiento": "XXXX-XX-XX",
        "viviendas": [
            {"id": 201, "direccion": "Calle 3"},
            {"id": 202, "direccion": "Calle 4"},
        ],
    },
    # Agrega más usuarios según sea necesario
]

# Ruta para obtener todas las viviendas de un usuario por ID
@Users_Houses.route('/api/usuarios/<int:usuario_id>/viviendas', methods=['GET'])
def obtener_viviendas(usuario_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)
    
    if usuario:
        return jsonify({"viviendas": usuario.get("viviendas", [])})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    Users_Houses.run(debug=True)


#En este caso, hemos agregado una lista de viviendas dentro de cada objeto de usuario. La nueva ruta es /api/usuarios/<int:usuario_id>/viviendas, donde <int:usuario_id> es el ID del usuario.

#Cuando se accede a esta ruta, la aplicación buscará el usuario por ID y devolverá la lista de viviendas asociadas a ese usuario según el ID del usuario introducido en la URL. 