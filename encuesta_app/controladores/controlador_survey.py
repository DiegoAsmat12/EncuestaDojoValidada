from flask import flash, render_template, request, redirect, session
from encuesta_app import app
from encuesta_app.modelos.modelo_survey import Survey

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def submitDojoSurvey():
    registro = {
        "nombre": request.form["nombre"],
        "ubicacion": request.form["ubicacion"],
        "idioma": request.form["idioma"],
        "comentario": request.form["comentario"]
    }
    if(Survey.validarRegistro(registro)):
        respuesta = Survey.crearRespuesta(registro)
        if(type(respuesta) is bool and not respuesta):
            print("Algo salio mal, intente nuevamente")
            return redirect("/")
        return redirect("/result")
    return redirect("/")

@app.route('/result')
def showSurveyResult():
    ultimoRegistro = Survey.obtenerUltimoRegistro()
    return render_template("info.html", registro = ultimoRegistro)

@app.route("/", methods=["POST"])
def resetData():
    return redirect("/")
