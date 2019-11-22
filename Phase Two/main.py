# [START imports]
from flask import Flask, render_template, request
import sqlalchemy
import os



db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

app = Flask(__name__)


##this is for testing
db = sqlalchemy.create_engine("mysql+pymysql://root:password@/test?127.0.0.1/" + str(cloud_sql_connection_name))

##This is for deployment
# db = sqlalchemy.create_engine(
#     # Equivalent URL:
#     # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
#     sqlalchemy.engine.url.URL(
#         drivername='mysql+pymysql',
#         username=db_user,
#         password=db_pass,
#         database=db_name,
#         query={
#             'unix_socket': '/cloudsql/{}'.format(cloud_sql_connection_name)
#         }
#     )
# )


## We should have a route for each query
@app.route('/', methods=["GET"])
def main():

    return render_template("index.html")

    # try: 
    #     with db.connect() as conn:
    #         num = conn.execute("Select * from testTable").fetchall()
    #         return str(num)

    # except Exception as e:
    #     return "it broke " + str(e)

        

if __name__=='__main__':    
    app.run(debug=True)