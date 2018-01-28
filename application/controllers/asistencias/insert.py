import config


class Insert():

    def __init__(self):
        pass

    def GET(self):
        return config.render.insert()

    def POST(self):
        form = config.web.input()

        config.model.insert_asistencias(
            form['id_alumno'],form['fecha'],form['asistio'],
        )
        raise config.web.seeother('/asistencias')
