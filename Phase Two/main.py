# [START imports]
from flask import Flask, render_template, request
import sqlalchemy
import os



db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

app = Flask(__name__)

db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername='mysql+pymysql',
        username=db_user,
        password=db_pass,
        database=db_name,
        query={
            'unix_socket': '/cloudsql/{}'.format(cloud_sql_connection_name)
        }
    )
)
# [END cloud_sql_mysql_sqlalchemy_create]


@app.route('/', methods=["GET"])
def main():

    try: 
        with db.connect() as conn:
            num = conn.execute("Select * from testTable").fetchall()
            return str(num)

    except Exception as e:
        return "it broke" + str(e)

        

if __name__=='__main__':    
    app.run()