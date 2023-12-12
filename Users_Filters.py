from flask import Flask, jsonify, request

Users_Filters = Flask(__name__)

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

# Ruta para obtener todas las viviendas de un usuario aplicando filtros opcionales
@Users_Filters.route('/api/usuarios/<int:usuario_id>/viviendas', methods=['GET'])
def obtener_viviendas(usuario_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)
    
    if not usuario:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    # Obtener parámetros de consulta opcionales
    ciudad = request.args.get('ciudad')
    calle = request.args.get('calle')
    pais = request.args.get('pais')

    # Filtrar viviendas basadas en los parámetros opcionales
    viviendas_filtradas = usuario.get("viviendas", [])

    if ciudad:
        viviendas_filtradas = [vivienda for vivienda in viviendas_filtradas if vivienda.get('ciudad') == ciudad]

    if calle:
        viviendas_filtradas = [vivienda for vivienda in viviendas_filtradas if vivienda.get('direccion') == calle]

    if pais:
        viviendas_filtradas = [vivienda for vivienda in viviendas_filtradas if vivienda.get('pais') == pais]

    return jsonify({"viviendas": viviendas_filtradas})

if __name__ == '__main__':
    Users_Filters.run(debug=True)


#Se han agregado parámetros de consulta opcionales (ciudad, calle, pais) y luego filtramos las viviendas en función de estos parámetros. 