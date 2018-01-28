import config
import app


class Edit:
    def __init__(self):
        pass

    def GET(self, id_alumno, message=None):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_EDIT(id_alumno)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    def POST(self, id_alumno, message=None):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.POST_EDIT(id_alumno)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_EDIT(id_alumno, message=None):
        id_alumno = config.check_secure_val(str(id_alumno))
        result = config.model.get_alumnos(int(id_alumno))
        result.id_alumno = config.make_secure_val(str(result.id_alumno))
        return config.render.edit(result, message)

    @staticmethod
    def POST_EDIT(id_alumno, message=None):
        form = config.web.input()
        form['id_alumno'] = config.check_secure_val(str(form['id_alumno']))
        res = config.model.edit_alumnos(
            form['id_alumno'],
            form['nombre_alumno'],
            form['matricula'],
            form['grupo'],
            form['nombre_padre'],
            form['direccion'],
            form['telefono'],
            form['id_telegram']
        )
        if res == 0:
            id_alumno = config.check_secure_val(str(id_alumno))
            result = config.model.get_alumnos(int(id_alumno))
            result.id_alumno = config.make_secure_val(str(result.id_alumno))
            message = "Error al editar el registro"
            return config.render.edit(result, message)
        else:
            raise config.web.seeother('/alumnos')
