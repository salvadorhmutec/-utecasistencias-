import config
import app

class Insert():

    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_INSERT()
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    def POST(self):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.POST_INSERT()
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_INSERT():
        return config.render.insert()

    @staticmethod
    def POST_INSERT():
        form = config.web.input()

        config.model.insert_alumnos(
            form['nombre_alumno'],
            form['matricula'],
            form['grupo'],
            form['nombre_padre'],
            form['direccion'],
            form['telefono'],
            form['id_telegram']
        )
        raise config.web.seeother('/alumnos')
