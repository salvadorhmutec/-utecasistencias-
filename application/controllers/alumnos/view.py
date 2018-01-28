import config
import app

class View:

    def __init__(self):
        pass

    def GET(self, id_alumno):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_VIEW(id_alumno)
            elif privilege == 1:
                raise config.web.seeother('/vendor')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_VIEW(id_alumno):
        id_alumno = config.check_secure_val(str(id_alumno))
        result = config.model.get_alumnos(id_alumno)
        return config.render.view(result)
