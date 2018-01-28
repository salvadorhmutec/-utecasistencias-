import config


class Delete:

    def GET(self, id_asistencia, message=None):
        id_asistencia = config.check_secure_val(str(id_asistencia))
        result = config.model.get_asistencias(int(id_asistencia))
        result.id_asistencia = config.make_secure_val(str(result.id_asistencia))
        return config.render.delete(result, message)

    def POST(self, id_asistencia, message=None):
        form = config.web.input()
        form['id_asistencia'] = config.check_secure_val(str(form['id_asistencia']))
        res = config.model.delete_asistencias(form['id_asistencia'])
        if res is None:
            message = "El registro no se puede borrar"
            id_asistencia = config.check_secure_val(str(id_asistencia))
            result = config.model.get_asistencias(int(id_asistencia))
            result.id_asistencia = config.make_secure_val(str(result.id_asistencia))
            return config.render.delete(result, message)
        else:
            raise config.web.seeother('/asistencias')

