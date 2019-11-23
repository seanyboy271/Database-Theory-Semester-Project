# [START imports]
from flask import Flask, render_template, request,json
import sqlalchemy
import os
import pandas as pd



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

# 1
# Input: 
# Output: 
@app.route('/', methods=["GET"])

# 2
# Input: 
# Output: 
@app.route('/', methods=["GET"])

# 3
# Input: 
# Output: 
@app.route('/', methods=["GET"])


# 4
# Input: 
# Output: 
@app.route('/', methods=["GET"])

# 5
# Input: 
# Output:
@app.route('/', methods=["GET"])

# 6
# Input: 
# Output:
@app.route('/', methods=["GET"])

# 7
# Input: 
# Output:
@app.route('/', methods=["GET"])

# 8
# Input: 
# Output:
@app.route('/', methods=["GET"])

# 9
# Input: 
# Output:
@app.route('/', methods=["GET"])

# 10
# Input: 
# Output:
@app.route('/', methods=["GET"])


# 11
# Input: PCName
# Output: unitNumber
@app.route('/VehicleWithPC', methods=["GET"])
def VehicleWithPC():
    args = request.args
    PCName = args['PCName']

    try:
        with db.connect() as conn:
            query = 'select v.unitNumber from Vehicle v join VehicleComputer c on v.unitNumber = c.unitNumber join MobileComputer MC on c.serialNumber = MC.serialNumber where PCName = \'' + PCName + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)

# 12
# Input: PCName
# Output: serialNumber
@app.route('/PCSerialNumber', methods=["GET"])
def PCSerialNumber():
    args = request.args
    PCName = args['PCName']

    try:
        with db.connect() as conn:
            query = 'Select serialNumber from MobileComputer where PCName = \'' + PCName + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# 13
# Input: unitNumber
# Output: Cradlepoint card number
@app.route('/CradlePointCardNumber', methods=["GET"])
def CradlePointCardNumber():
    args = request.args
    unitNumber = args['unitNumber']

    try:
        with db.connect() as conn:
            query = 'Select serialNumber from MobileComputer where PCName = \'' + PCName + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# 14
# Input: None
# Output: Number of computers being used by IT
@app.route('/ITComputers', methods=["GET"])
def ITComputers():
    try:
        with db.connect() as conn:
            query = 'select count(serialNumber) as "Number of Computers" from MobileComputer where PCName = \"IT\"'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)

# 15
# Input: PCName
# Output: bitlocker key
@app.route('/BitlockerKey', methods=["GET"])
def BitlockerKey():
    args = request.args
    PCName = args['PCName']

    try:
        with db.connect() as conn:
            query = 'Select bitLockerKey from MobileComputer where PCName = \'' + PCName +  '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# 16
# Input: None
# Output: Cars with short dock stands
@app.route('/VehiclesWithShortDock', methods=["GET"])
def VehiclesWithShortDock():
    try:
        with db.connect() as conn:
            query = 'select V.* from Dock join MobileComputerDock MCD on Dock.SerialNumber = MCD.dock_serialNumber join MobileComputer MC on MCD.computer_serialNumber = MC.serialNumber join VehicleComputer VC on MC.serialNumber = VC.serialNumber join Vehicle V on VC.unitNumber = V.unitNumber where Dock.standType = "short"'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



# 17
# Input: None
# Output: Number of vehicles with front and rear arbitrator systems
@app.route('/VehiclesWithFrontAndRearCamera', methods=["GET"])
def VehiclesWithFrontAndRearCamera():
    try:
        with db.connect() as conn:
            query = 'select count(VAS.unitNumber) as "Number of Vehicles" from ArbitratorSystem join VehicleArbitratorSystem VAS on ArbitratorSystem.ID = VAS.ID where hasFrontCamera = TRUE and hasRearCamera = TRUE'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# 18
# Input: unitNumber
# Output: Number of Bad Bois caught
@app.route('/BadBois', methods=["GET"])
def BadBois():
    args = request.args
    unitNumber = args['unitNumber']

    try:
        with db.connect() as conn:
            query = 'select badBoysCaught from Vehicle where unitNumber = \'' + unitNumber + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# 19
# Input: None
# Output: Computers that have a keyboard but no computer
@app.route('/VehiclesWithKeyboardAndNoComputer', methods=["GET"])
def VehiclesWithKeyboardAndNoComputer():
    try:
        with db.connect() as conn:
            query = 'select * from Vehicle join VehicleKeyboard on Vehicle.unitNumber = VehicleKeyboard.unitNumber where Vehicle.unitNumber not in(select Vehicle.unitNumber from Vehicle join VehicleComputer on Vehicle.unitNumber = VehicleComputer.unitNumber)'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# 20
# Input: None
# Output: Arbitrator systems with bad status codes
@app.route('/ArbitratorWithBadStatusCodes', methods=["GET"])
def ArbitratorWithBadStatusCodes():
    try:
        with db.connect() as conn:
            query = 'select * from ArbitratorSystem join ArbitratorSystemFrontCamera ASFC on ArbitratorSystem.ID = ASFC.ID join ArbitratorSystemRearCamera ASRC on ArbitratorSystem.ID = ASRC.ID join FrontCamera FC on ASFC.CameraID = FC.cameraID join RearCamera RC on ASRC.CameraID = RC.cameraID where FC.status = "Broken" or RC.status = "Broken"'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



@app.route('/vehicle', methods=["GET"])
def vehicles():

    return render_template("vehicle.html")


@app.route('/vehicle/all', methods=["GET"])
def vehicles_all():
    try:
        with db.connect() as conn:
            query = 'select * from Vehicle'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


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