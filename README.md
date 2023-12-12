# BCNC Example Api documentation
This project consists of 9 APIs with different functions and methods used to obtain or modify user data.


## Functions
Here you can find a description of each API and how it works.

| Api name | Funtionalities	|
| --------- | ---------- |
| Api_users          | Gets data from all existing users.                                                               |
| unique_user        | Gets data from a single user.                                                                    |
| Users_Houses       | Gets data from the users' homes.                                                                 |
| Users_Filters      | Gets data from all of a user's homes by applying the optional city, street, and country filters. |
| Create_User        | Create new users.                                                                                |
| Update_Users       | Updates partial user data.                                                                       |
| Update_Users_All   | Updates all user data.                                                                           |
| Manage_Info_Houses | Create, delete and update a user's homes.                                                        |
| Delete_Users       | Delete users.                                                                                    |

### Used Methods
- Api_users: Ingresando la URL en el navegador, mediante el método GET se obtiene una respuesta JSON con todos los usuarios.
usuarios = [
    {"id": 1, "nombre": "Usuario1", "correo": "usuario1@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    {"id": 2, "nombre": "Usuario2", "correo": "usuario2@example.com", "Fechanacimiento": "XXXX-XX-XX"},
    # Agrega más usuarios según sea necesario
]'
Create_User
Delete_Users
Manage_Info_Houses
unique_user
Update_Users
Update_Users_All
Users_Filters
Users_Houses
