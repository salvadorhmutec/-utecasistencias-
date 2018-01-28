import config


class Edit:

    def GET(self, id_asistencia, message=None):
        id_asistencia = config.check_secure_val(str(id_asistencia))
        result = config.model.get_asistencias(int(id_asistencia))
        result.id_asistencia = config.make_secure_val(str(result.id_asistencia))
        return config.render.edit(result, message)

    def POST(self, id_asistencia, message=None):
        form = config.web.input()
        form['id_asistencia'] = config.check_secure_val(str(form['id_asistencia']))
        res = config.model.edit_asistencias(
            form['id_asistencia'],form['id_alumno'],form['fecha'],form['asistio'],
        )
        if res == 0:
            id_asistencia = config.check_secure_val(str(id_asistencia))
            result = config.model.get_asistencias(int(id_asistencia))
            result.id_asistencia = config.make_secure_val(str(result.id_asistencia))
            message = "Error al editar el registro"
            return config.render.edit(result, message)
        else:
            raise config.web.seeother('/asistencias')