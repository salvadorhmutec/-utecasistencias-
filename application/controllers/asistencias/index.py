import app
import config
import telegram


class Index:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            grupo = app.session.grupo
            if privilege == 1:
                return self.GET_INDEX(grupo)
            elif privilege == 0:
                raise config.web.seeother('/')
        else:
            raise config.web.seeother('/login')
        
    def POST(self):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            grupo = app.session.grupo
            if privilege == 1:
                return self.POST_INDEX()
            elif privilege == 0:
                raise config.web.seeother('/')
        else:
            raise config.web.seeother('/login')
 
    @staticmethod
    def GET_INDEX(grupo):
        print "Asistencias del grupo ", grupo
        result_alumnos = config.model_alumnos.get_alumnos_grupo(grupo).list()
        result = config.model.get_all_asistencias().list()
        for row in result:
            row.id_asistencia = config.make_secure_val(str(row.id_asistencia))

        for row in result_alumnos:
            row.id_alumno = config.make_secure_val(str(row.id_alumno))

        return config.render.index(result, result_alumnos)

    @staticmethod
    def POST_INDEX():
        form = config.web.input(id_alumno=[], asistio=[])
        #token_samm = "336120290:AAH4gV1OtyYgvdpmR_Hk7W7cSBrapM05HbY"
        token_utec = "504256455:AAFPiLYboDv8YssiWwsxVeMxaM-PxGQLk74"
        
        bot = telegram.Bot(token=token_utec)
        for i in range(len(form['asistio'])):
            id_alumno = form['id_alumno'][i]
            if form['asistio'][i] == '0':
                asistio = 'no'
            else:
                asistio = 'si'
            id_alumno = config.check_secure_val(id_alumno)
            config.model.insert_asistencias(id_alumno, asistio)

            alumnos = config.model_alumnos.get_alumnos(id_alumno)

            nombre_alumno = alumnos.nombre_alumno
            id_telegram = alumnos.id_telegram


            text_alumno = "El alumno :" + nombre_alumno + " " + asistio + " asistio"
            status = bot.send_message(chat_id=id_telegram, text=text_alumno)
            print(status)
        raise config.web.seeother('/')
