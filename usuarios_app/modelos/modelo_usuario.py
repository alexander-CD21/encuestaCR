from usuarios_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, id,first_name , last_name,email,created_at,updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email= email
        self.created_at=created_at
        self.updated_at=updated_at

    @classmethod
    def agregarUsuario(cls,nuevoUsuario):
        query = "INSERT INTO users(first_name, last_name, email,created_at,updated_at) VALUES( %(first_name)s, %(last_name)s, %(email)s,NOW(),NOW());"
        resultado = connectToMySQL( "users_db" ).query_db(query,nuevoUsuario)
        return resultado 

    @classmethod
    def obtenerListaUsuario(cls):
        query = "SELECT * FROM users;"
        resultado = connectToMySQL( "users_db" ).query_db( query )
        print(resultado)
        listaUsuarios = []
        for usua in resultado:
            listaUsuarios.append( Usuario(usua["id"],usua["first_name"],usua["last_name"], usua["email"], usua["created_at"], usua["updated_at"] ) )
        return listaUsuarios
