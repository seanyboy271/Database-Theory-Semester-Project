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
db = sqlalchemy.create_engine("mysql+pymysql://root:password@/508ProjectDatabase?127.0.0.1/" + str(cloud_sql_connection_name))

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

    return render_template("dashboard.html")

    # try: 
    #     with db.connect() as conn:
    #         num = conn.execute("Select * from testTable").fetchall()
    #         return str(num)

    # except Exception as e:
    #     return "it broke " + str(e)

#11
#Input: PCName
#Output:unitNumber
@app.route('/VehicleWithPC', methods=["GET"])
def VehicleWithPC():
    query = 'select v.unitNumber from Vehicle v join VehicleComputer c on v.unitNumber = c.unitNumber join MobileComputer MC on c.serialNumber = MC.serialNumberwhere PCName = enter pc name here'

#12
#Input: PCName
#Output: serialNumber
@app.route('/PCSerialNumber', methods=["GET"])

#13
#Input: unitNumber
#Output: Cradlepoint card number
@app.route('/CradlePointCardNumber', methods=["GET"])

#14
#Input: None
#Output: Number of computers being used by IT
@app.route('/ITComputers', methods=["GET"])

#15
#Input: PCName
#Output: bitlocker key
@app.route('/BitlockerKey', methods=["GET"])

#16
#Input: None
#Output: Cars with short dock stands
@app.route('/VehiclesWithShortDock', methods=["GET"])

#17
#Input: None
#Output: Number of vehicles with front and rear arbitrator systems
@app.route('/VehiclesWithFrontAndRearCamera', methods=["GET"])

#18
#Input: unitNumber
#Output: Number of Bad Bois caught
@app.route('/BadBois', methods=["GET"])

#19
#Input: None
#Output: Computers that have a keyboard but no computer
@app.route('/VehiclesWithKeyboardAndNoComputer', methods=["GET"])

#20
#Input: None
#Output: Arbitrator systems with bad status codes
@app.route('/ArbitratorWithBadStatusCodes', methods=["GET"])    
@app.route('/vehicle', methods=["GET"])
def vehicles():

    return render_template("vehicle.html")

@app.route('/mobilecomputer', methods=["GET"])
def mobilecomputer():

    return render_template("mobilecomputer.html")

@app.route('/mobilecomputerdock', methods=["GET"])
def mobilecomputerdock():

    return render_template("mobilecomputerdock.html")

@app.route('/arbitrator', methods=["GET"])
def arbitrator():

    return render_template("arbitrator.html")


@app.route('/cradlepoint', methods=["GET"])
def cradlepoint():

    return render_template("cradlepoint.html")

@app.route('/keyboard', methods=["GET"])
def keyboard():

    return render_template("keyboard.html")

@app.route('/softwarestatus', methods=["GET"])
def softwarestatus():

    return render_template("softwarestatus.html")

@app.route('/frontcamera', methods=["GET"])
def frontcamera():

    return render_template("frontcamera.html")

@app.route('/backcamera', methods=["GET"])
def backcamera():

    return render_template("backcamera.html")


        

if __name__=='__main__':
    app.run(debug=True)