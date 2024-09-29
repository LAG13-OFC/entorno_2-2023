from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'app'
app.config['MYSQL_DATABASE_PASSWORD'] = '4PP1p3rs0ns'
app.config['MYSQL_DATABASE_DB'] = 'api-persons'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)