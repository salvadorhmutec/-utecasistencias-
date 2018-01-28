import app
import config

class Index:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            grupo = app.session.grupo
            if privilege == 0:
                return self.GET_INDEX(grupo)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_INDEX(grupo):
        result = config.model.get_all_alumnos().list()
        #result = config.model.get_alumnos_grupo(grupo).list()
        for row in result:
            row.id_alumno = config.make_secure_val(str(row.id_alumno))
        return config.render.index(result)