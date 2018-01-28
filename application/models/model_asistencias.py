import web
import config

db = config.db


def get_all_asistencias():
    try:
        return db.select('asistencias')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_asistencias(id_asistencia):
    try:
        return db.select('asistencias', where='id_asistencia=$id_asistencia', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_asistencias(id_asistencia):
    try:
        return db.delete('asistencias', where='id_asistencia=$id_asistencia', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None

"""
def insert_asistencias(id_alumno,fecha,asistio):
    try:
        return db.insert('asistencias',id_alumno=id_alumno,
fecha=fecha,
asistio=asistio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None
"""

def insert_asistencias(id_alumno,asistio):
    try:
        return db.insert('asistencias',
            id_alumno=id_alumno,
            asistio=asistio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None

def edit_asistencias(id_asistencia,id_alumno,fecha,asistio):
    try:
        return db.update('asistencias',id_asistencia=id_asistencia,
id_alumno=id_alumno,
fecha=fecha,
asistio=asistio,
                  where='id_asistencia=$id_asistencia',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
