from encuesta_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
class Survey:
    def __init__(self,id, nombre, ubicacion, idioma, comentario, created_at, updated_at):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.idioma = idioma
        self.comentario = comentario
        self.created_at = created_at
        self.updated_at = updated_at
        
    @classmethod
    def crearRespuesta(cls, encuesta):
        query = '''
                    INSERT INTO dojos(nombre,ubicacion,idioma,comentario,created_at,updated_at)
                    VALUES (%(nombre)s, %(ubicacion)s, %(idioma)s, %(comentario)s, NOW(), NOW());
                '''
        respuesta = connectToMySQL("esquema_encuesta_dojo").query_db(query,encuesta)
        return respuesta

    @classmethod
    def obtenerUltimoRegistro(cls):
        query = '''
                    SELECT * FROM dojos
                    ORDER BY dojos.id DESC 
                    LIMIT 1;
                '''
        respuesta = connectToMySQL("esquema_encuesta_dojo").query_db(query)
        survey = cls(respuesta[0]["id"], respuesta[0]["nombre"], respuesta[0]["ubicacion"],
            respuesta[0]["idioma"], respuesta[0]["comentario"], respuesta[0]["created_at"],
            respuesta[0]["updated_at"])

        return survey

    @staticmethod
    def validarRegistro(registro):
        isValid = True
        if(len(registro["nombre"])<3):
            flash("El nombre debe tener almenos 3 carcateres.")
            isValid=False
        if(len(registro["ubicacion"])<1):
            flash("Debes escoger una ubicación.")
            isValid=False
        if(len(registro["idioma"])<1):
            flash("Debes escoger un lenguaje favorito.")
            isValid=False
        if(len(registro["comentario"])<3):
            flash("El comentario debe tener almenos 3 carcateres.")
            isValid=False
        return isValid