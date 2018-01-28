from telegram.ext import Updater, CommandHandler
import web

'''
db_host = 'localhost'
db_name = 'bot_asistencia'
db_user = 'kuorra'
db_pw = 'kuorra.2017'
'''

db_host = 'fugfonv8odxxolj8.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'eftaz6n2sqv292f7'
db_user = 'yg9mvid1uls20vfz'
db_pw = 'abdhhbjou44g6l4k'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )

def edit_alumno(id_alumno, id_telegram):
    try:
        return db.update('alumnos',
                    id_alumno=id_alumno,
                    id_telegram=id_telegram,
                    where='id_alumno=$id_alumno',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None

def get_alumno(id_alumno):
    try:
        return db.select('alumnos', where='id_alumno=$id_alumno', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None

def alta(bot, update):
    id_alumno = update.message.text.split()[1]
    print id_alumno
    edit_alumno(id_alumno, update.message.from_user.id )
    alumno = get_alumno(id_alumno)
    nombre_alumno = alumno.nombre_alumno
    grupo = alumno.grupo
    update.message.reply_text(
        'Alta completada con exito del alumno {} del grupo {}'.format(nombre_alumno, grupo))

def main():
    token_utec = "504256455:AAFPiLYboDv8YssiWwsxVeMxaM-PxGQLk74"
    #token_samm = "336120290:AAH4gV1OtyYgvdpmR_Hk7W7cSBrapM05HbY"
    updater = Updater(token_utec)

    updater.dispatcher.add_handler(CommandHandler('alta', alta))

    updater.start_polling()
    updater.idle()
    print "BOT funcionando"

if __name__ == '__main__':
    main()
