import sqlalchemy as db

class DbConnection():

    def connector():

        config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'apimastery'
        }

        db_user = config.get('user')
        db_pwd = config.get('password')
        db_host = config.get('host')
        db_port = config.get('port')
        db_name = config.get('database')

        # specify connection string
        connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

        # # connect to database
        # engine = db.create_engine(connection_str)
        # connection = engine.connect()

        return connection_str