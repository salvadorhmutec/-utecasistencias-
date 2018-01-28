'''
    Bienvenida al sistema
'''
import app
from . import config

class Index:
    def __init__(self):
        pass

    @staticmethod
    def GET():
        if app.session.loggedin is True:
            username = app.session.username
            privilege = app.session.privilege
            grupo = app.session.grupo
            params = {}
            params['username'] = username
            params['privilege'] = privilege
            params['grupo'] = grupo
            if privilege == 0:
                return config.render.admin(params)
            elif privilege == 1:
                return config.render.guess(params)
        else:
            params = {}
            params['username'] = 'anonymous'
            params['privilege'] = '-1'
            params['grupo'] = 'na'
            return config.render.index(params)
