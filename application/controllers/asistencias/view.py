import config


class View:

    def GET(self, id_asistencia):
        id_asistencia = config.check_secure_val(str(id_asistencia))
        result = config.model.get_asistencias(id_asistencia)
        return config.render.view(result)