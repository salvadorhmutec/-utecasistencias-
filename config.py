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