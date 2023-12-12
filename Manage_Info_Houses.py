from flask import Flask, jsonify, request

Manage_Info_Houses = Flask(__name__)

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

# Ruta para obtener todas las viviendas de un usuario por ID
@Manage_Info_Houses.route('/api/usuarios/<int:usuario_id>/viviendas', methods=['GET'])
def obtener_viviendas(usuario_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)

    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    return jsonify({"viviendas": usuario.get("viviendas", [])})

# Ruta para crear una nueva vivienda para un usuario
@Manage_Info_Houses.route('/api/usuarios/<int:usuario_id>/viviendas', methods=['POST'])
def crear_vivienda(usuario_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)

    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    nueva_vivienda = {
        "id": len(usuario["viviendas"]) + 1,
        "direccion": request.json.get('direccion'),
        "ciudad": request.json.get('ciudad'),
        "pais": request.json.get('pais'),
    }

    usuario["viviendas"].append(nueva_vivienda)

    return jsonify({"mensaje": "Vivienda creada exitosamente", "vivienda": nueva_vivienda}), 201

# Ruta para borrar una vivienda de un usuario por ID de vivienda
@Manage_Info_Houses.route('/api/usuarios/<int:usuario_id>/viviendas/<int:vivienda_id>', methods=['DELETE'])
def borrar_vivienda(usuario_id, vivienda_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)

    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    vivienda = next((v for v in usuario["viviendas"] if v["id"] == vivienda_id), None)

    if not vivienda:
        return jsonify({"mensaje": "Vivienda no encontrada"}), 404

    usuario["viviendas"].remove(vivienda)

    return jsonify({"mensaje": "Vivienda borrada exitosamente"})

# Ruta para actualizar completamente una vivienda de un usuario por ID de vivienda
@Manage_Info_Houses.route('/api/usuarios/<int:usuario_id>/viviendas/<int:vivienda_id>', methods=['PUT'])
def actualizar_vivienda(usuario_id, vivienda_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)

    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    vivienda = next((v for v in usuario["viviendas"] if v["id"] == vivienda_id), None)

    if not vivienda:
        return jsonify({"mensaje": "Vivienda no encontrada"}), 404

    datos_actualizados = request.json
    vivienda.update(datos_actualizados)

    return jsonify({"mensaje": "Vivienda actualizada completamente", "vivienda": vivienda})

if __name__ == '__main__':
    Manage_Info_Houses.run(debug=True)

#Se han agregado rutas para crear, borrar y actualizar viviendas asociadas a un usuario específico