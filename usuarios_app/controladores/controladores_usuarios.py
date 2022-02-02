from flask import Flask,render_template,redirect,session,flash,request
from usuarios_app import app
from usuarios_app.modelos.modelo_usuario import Usuario

@app.route('/' , methods=['GET'])
def raiz():
    return redirect('/users')

@app.route('/users' , methods=["GET"])
def leerDatos():
        listaUsuarios=Usuario.obtenerListaUsuario()
        return render_template("leer.html",usuario=listaUsuarios)

@app.route('/users/new' , methods=["GET"])
def datos():
    return render_template("crear.html")

@app.route('/users/create', methods=['POST'])
def creaDatos():
    nuevoUsuario={
        "first_name" : request.form[ "first_name" ],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["email"] = request.form["email"]
    Usuario.agregarUsuario(nuevoUsuario)
    return redirect('/users')
