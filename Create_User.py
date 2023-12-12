from flask import Flask, jsonify, request

Create_User = Flask(__name__)

# Datos de ejemplo
usuarios = [
    {"id": 1, "nombre": "Usuario1", "correo": "usuario1@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    {"id": 2, "nombre": "Usuario2", "correo": "usuario2@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    # Agrega más usuarios según sea necesario
]

# Ruta para obtener todos los usuarios
@Create_User.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

# Ruta para crear un nuevo usuario
@Create_User.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": request.json.get('nombre'),
        "correo": request.json.get('correo'),
        "Fechanacimiento": request.json.get('Fechanacimiento'),
    }

    usuarios.append(nuevo_usuario)

    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}), 201

if __name__ == '__main__':
    Create_User.run(debug=True)


#Se ha agregado una nueva ruta (/api/usuarios) con el método POST para crear un nuevo usuario. Cuando haces una solicitud POST a esta ruta con datos JSON en el cuerpo de la solicitud, se crea un nuevo usuario y se agrega a la lista de usuarios.