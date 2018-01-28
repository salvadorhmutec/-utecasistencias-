# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/alumnos', 'application.controllers.alumnos.index.Index',
    '/alumnos/view/(.+)', 'application.controllers.alumnos.view.View',
    '/alumnos/edit/(.+)', 'application.controllers.alumnos.edit.Edit',
    '/alumnos/delete/(.+)', 'application.controllers.alumnos.delete.Delete',
    '/alumnos/insert', 'application.controllers.alumnos.insert.Insert',
    '/asistencias', 'application.controllers.asistencias.index.Index',
    '/asistencias/view/(.+)', 'application.controllers.asistencias.view.View',
    '/asistencias/edit/(.+)', 'application.controllers.asistencias.edit.Edit',
    '/asistencias/delete/(.+)', 'application.controllers.asistencias.delete.Delete',
    '/asistencias/insert', 'application.controllers.asistencias.insert.Insert',
    '/samm','application.bot.samm.Samm'
)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

store = web.session.DiskStore('sessions')

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class count:
    def GET(self):
        session.count += 1
        return str(session.count)


def internalerror():
    raise config.web.seeother('/')


def notfound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False
    web.config.debug = False
    web.config.db_printing = False
    app.internalerror = internalerror
    app.notfound = notfound
    app.run()
