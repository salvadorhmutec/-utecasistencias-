from subprocess import call

class Samm:
    def __init__(self):
        pass

    def GET(self):
        call(['python samm_bot.py'], shell = True)
        return 'S.A.M.M'
