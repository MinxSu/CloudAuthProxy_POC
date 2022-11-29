import sqlalchemy
import configparser
from google.cloud.sql.connector import Connector

# configs
config = configparser.ConfigParser()
config.read('config.ini')

# os.environ["INSTANCE_CONNECTION_NAME"]  # e.g. 'project:region:instance'
INSTANCE_CONNECTION_NAME = config['PostgreSQL']['INSTANCE_CONNECTION_NAME']
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = config['PostgreSQL']['DB_USER'] # e.g. 'my-db-user'
DB_PASS = config['PostgreSQL']['DB_PASS'] # e.g. 'my-db-password'
DB_NAME = config['PostgreSQL']['DB_NAME'] # e.g. 'my-database'

# initialize Connector object
connector = Connector()

def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pg8000",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

def test():
    try:
        with pool.connect() as db_conn:
            results = db_conn.execute("SELECT NOW()").fetchone()
            return results[0]
    except Exception as message:
        print(message)
        return message