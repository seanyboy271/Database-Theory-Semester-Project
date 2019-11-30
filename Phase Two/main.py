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

# Login Route
# This can be fairly simple, although we should not store the plain text passwords since she wants security
# We also need to figure out how to give permissions to certain users
@app.route('/login', methods=["GET"])
def login():
    args = request.args
    userName = args["username"]
    password = args["password"]
    query = 'Select type from Users where username = \'' + userName + '\' and password = encode( \'' + password + '\', \'encryptKey\')'

    try:
        with db.connect() as conn:
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



#We need to have an update, delete, and insert for each 'major' table i.e vehicle, mobile computer, keyboards, dock, etc... There are 9 major tables, so 27 endpoints
# We could use stored procedures for this so that it is possible to keep the linking tables updated with the new data.
# We could use triggers in place of the check() constraint to make sure tha data is valid
# We could use views for the enpoints that dont take in any form of input or for very commonly used joins


# @app.route('/Insert_______', methods=["POST"])
# def Insert____________():
#     ##insert template


# @app.route('/Delete_______', methods=["DELETE"])
# def Delete___________():
#     ##Delete template


# @app.route('/Update__________', methods=["PUT"])
# def Update____________():
#     ##Update template



## 20 QUERIES
# 1
# Input: None 
# Output: unitNumber, lastVideoUploadDate
@app.route('/VehicleWithRecentlyUploaded', methods=["GET"])
def VehicleWithRecentlyUploaded():
    try:
        with db.connect() as conn:
            query = 'Select * from VehicleWithRecentlyUploadedView'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



# 2
# Input: gpsComPort
# Output: unitNumber
@app.route('/VehiclesOnComPort', methods=["GET"])
def VehiclesOnComPort():
    args = request.args
    gpsComPort = args['gpsComPort']

    try:
        with db.connect() as conn:
            query = 'SELECT V.unitNumberFROM Vehicle V JOIN VehicleComputer VC ON V.unitNumber = VC.unitNumber JOIN MobileComputer C ON C.serialNumber = VC.serialNumber WHERE gpsComPort = \'' + gpsComPort + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# 3
# Input: unitNumber
# Output: cableColor
@app.route('/CradlepointCableColor', methods=["GET"])
def CradlepointCableColor():
    args = request.args
    unitNumber = args['unitNumber']

    try:
        with db.connect() as conn:
            query = 'SELECT cableColor FROM VehicleCradlepoint NATURAL JOIN CradlePoint WHERE VehicleCradlepoint.unitNumber = \'' + unitNumber + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



# 4
# Input: unitNumber
# Output: PCName
@app.route('/PCNameInVehicle', methods=["GET"])
def PCNameInVehicle():
    args = request.args
    unitNumber = args['unitNumber']

    try:
        with db.connect() as conn:
            query = 'SELECT PCName FROM MobileComputer MC JOIN VehicleComputer VC ON MC.serialNumber = VC.serialNumber JOIN Vehicle V ON VC.unitNumber = V.unitNumber WHERE V.unitNumber = \'' + unitNumber + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# 5
# Input: None
# Output: unitNumber
@app.route('/NewestArbitratorVersionVehicle', methods=["GET"])
def NewestArbitratorVersionVehicle():
    try:
        with db.connect() as conn:
            query = 'Select * from NewestArbitratorVersionVehicleView'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



# 6
# Input: mobileComputerSerialNumber
# Output: computer model
@app.route('/MobileComputerModel', methods=["GET"])
def MobileComputerModel():
    args = request.args
    serialNumber = args['serialNumber']

    try:
        with db.connect() as conn:
            query = 'SELECT model FROM MobileComputer WHERE serialNumber = \'' + serialNumber + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



# 7
# Input: keyboard serial number
# Output: hasStickyKeys
@app.route('/HasStickyKeys', methods=["GET"])
def HasStickyKeys():
    args = request.args
    serialNumber = args['serialNumber']

    try:
        with db.connect() as conn:
            query = 'SELECT hasStickyKeys FROM Keyboard WHERE serialNumber = \'' + serialNumber + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



# 8
# Input: PCName
# Output: dock serialNumber
@app.route('/ComputerDock', methods=["GET"])
def ComputerDock():
    args = request.args
    PCName = args['PCName']

    try:
        with db.connect() as conn:
            query = 'SELECT D.serialNumber FROM Dock D JOIN MobileComputerDock MCD ON D.serialNumber = MCD.dock_serialNumber JOIN MobileComputer MC ON MCD.computer_serialNumber = MC.serialNumber WHERE MC.PCName = \'' + PCName + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



# 9
# Input: unitNumber
# Output: lastModifyDate
@app.route('/LatModifyDate', methods=["GET"])
def LatModifyDate():
    args = request.args
    unitNumber = args['unitNumber']

    try:
        with db.connect() as conn:
            query = 'SELECT lastModifyDate FROM Vehicle WHERE unitNumber = \'' + unitNumber + '\''
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)



# 10
# Input: none
# Output: unitNumber, lastModifyDate
@app.route('/VehcleWithOldestInpectionDate', methods=["GET"])
def VehcleWithOldestInpectionDate():
    try:
        with db.connect() as conn:
            query = 'Select * from VehcleWithOldestInpectionDateView'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)
    


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
            query = 'select VC.cardNumber from CradlePoint join VehicleCradlepoint VC on CradlePoint.cardNumber = VC.cardNumber join Vehicle V on VC.unitNumber = V.unitNumber where V.unitNumber =\'' + unitNumber + '\''
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
            query = 'Select * from ITComputersView'
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
# Input: dockType
# Output: Cars with short dock stands
@app.route('/VehiclesWithDockType', methods=["GET"])
def VehiclesWithDockType():
    args = request.args
    dockType = args["dockType"]

    try:
        with db.connect() as conn:
            query = 'select V.* from Dock join MobileComputerDock MCD on Dock.SerialNumber = MCD.dock_serialNumber join MobileComputer MC on MCD.computer_serialNumber = MC.serialNumber join VehicleComputer VC on MC.serialNumber = VC.serialNumber join Vehicle V on VC.unitNumber = V.unitNumber where Dock.standType = \'' + dockType + '\''
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
            query = 'Select * from VehiclesWithFrontAndRearCameraView'
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
            query = 'Select * from VehiclesWithKeyboardAndNoComputerView'
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
            query = 'Select * from ArbitratorWithBadStatusCodesView'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# Vehicles
@app.route('/vehicles', methods=["GET"])
def vehicles():

    return render_template("vehicles.html")

@app.route('/vehicle/<id>', methods=["GET"])
def vehicle_id(id):
    try:
        with db.connect() as conn:
            query = 'select * from Vehicle where unitNumber = \"' + id + '\"'
            result = conn.execute(query).fetchall()
            res = json.dumps([dict(r) for r in result])

    except Exception as e:
        res = ""

    return render_template("vehicle.html", unitNum=id, data=res)


@app.route('/vehicle/all', methods=["GET"])
def vehicles_all():
    try:
        with db.connect() as conn:
            query = 'select * from Vehicle'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# Mobile Computers
@app.route('/mobilecomputers', methods=["GET"])
def mobilecomputer():

    return render_template("mobilecomputers.html")

@app.route('/mobilecomputer/<serialNumber>', methods=["GET"])
def mobilecomputer_id(serialNumber):
    try:
        with db.connect() as conn:
            query = 'select * from MobileComputer where serialNumber = \"' + serialNumber + '\"'
            result = conn.execute(query).fetchall()
            res = json.dumps([dict(r) for r in result])

    except Exception as e:
        res = ""

    return render_template("mobilecomputer.html", unitNum=id, data=res)

@app.route('/mobilecomputer/all', methods=["GET"])
def mobilecomputer_all():
    try:
        with db.connect() as conn:
            query = 'select * from MobileComputer'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)

@app.route('/mobilecomputerdocks', methods=["GET"])
def mobilecomputerdock():

    return render_template("mobilecomputerdocks.html")

@app.route('/mobilecomputerdock/<serialNumber>', methods=["GET"])
def mobilecomputerdock_id(serialNumber):
    try:
        with db.connect() as conn:
            query = 'select * from Dock where SerialNumber = \"' + serialNumber + '\"'
            result = conn.execute(query).fetchall()
            res = json.dumps([dict(r) for r in result])

    except Exception as e:
        res = ""

    return render_template("mobilecomputerdock.html", unitNum=id, data=res)

@app.route('/mobilecomputerdock/all', methods=["GET"])
def mobilecomputerdock_all():
    try:
        with db.connect() as conn:
            query = 'select * from Dock'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)

@app.route('/arbitrators', methods=["GET"])
def arbitrator():

    return render_template("arbitrators.html")

@app.route('/arbitrator/<id>', methods=["GET"])
def arbitrator_id(id):
    try:
        with db.connect() as conn:
            query = 'select * from ArbitratorSystem where id = \"' + id + '\"'
            result = conn.execute(query).fetchall()
            res = json.dumps([dict(r) for r in result])

    except Exception as e:
        res = ""

    return render_template("arbitrator.html", unitNum=id, data=res)

@app.route('/arbitrator/all', methods=["GET"])
def arbitrator_all():
    try:
        with db.connect() as conn:
            query = 'select * from ArbitratorSystem'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)

# Cradlepoint
@app.route('/cradlepoints', methods=["GET"])
def cradlepoint():

    return render_template("cradlepoints.html")

@app.route('/cradlepoint/<cardNumber>', methods=["GET"])
def cradlepoint_id(cardNumber):
    try:
        with db.connect() as conn:
            query = 'select * from CradlePoint where cardNumber = \"' + cardNumber + '\"'
            result = conn.execute(query).fetchall()
            res = json.dumps([dict(r) for r in result])

    except Exception as e:
        res = ""

    return render_template("cradlepoint.html", unitNum=id, data=res)

@app.route('/cradlepoint/all', methods=["GET"])
def cradlepoint_all():
    try:
        with db.connect() as conn:
            query = 'select * from CradlePoint'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


# Keyboard
@app.route('/keyboards', methods=["GET"])
def keyboard():

    return render_template("keyboards.html")

@app.route('/keyboard/<serialNumber>', methods=["GET"])
def keyboard_id(serialNumber):
    try:
        with db.connect() as conn:
            query = 'select * from Keyboard where serialNumber = \"' + serialNumber + '\"'
            result = conn.execute(query).fetchall()
            res = json.dumps([dict(r) for r in result])

    except Exception as e:
        res = ""

    return render_template("keyboard.html", unitNum=id, data=res)

@app.route('/keyboard/all', methods=["GET"])
def keyboard_all():
    try:
        with db.connect() as conn:
            query = 'select * from Keyboard'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)

@app.route('/softwarestatus/<serialNumber>', methods=["GET"])
def softwarestatus(serialNumber):
    try:
        with db.connect() as conn:
            query = 'select * from ComputerSoftwareStatus where serialNumber = \"' + serialNumber + '\"'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)

# Front Camera
@app.route('/frontcameras', methods=["GET"])
def frontcamera():

    return render_template("frontcameras.html")

@app.route('/frontcamera/<cameraID>', methods=["GET"])
def frontcamera_id(cameraID):
    try:
        with db.connect() as conn:
            query = 'select * from FrontCamera where cameraID = \"' + cameraID + '\"'
            result = conn.execute(query).fetchall()
            res = json.dumps([dict(r) for r in result])

    except Exception as e:
        res = ""

    return render_template("frontcamera.html", unitNum=id, data=res)

@app.route('/frontcamera/all', methods=["GET"])
def frontcamera_all():
    try:
        with db.connect() as conn:
            query = 'select * from FrontCamera'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)

# Rear Camera
@app.route('/rearcameras', methods=["GET"])
def rearcamera():

    return render_template("rearcameras.html")

@app.route('/rearcamera/<cameraID>', methods=["GET"])
def rearcamera_id(cameraID):
    try:
        with db.connect() as conn:
            query = 'select * from RearCamera where cameraID = \"' + cameraID + '\"'
            result = conn.execute(query).fetchall()
            res = json.dumps([dict(r) for r in result])

    except Exception as e:
        res = ""

    return render_template("rearcamera.html", unitNum=id, data=res)

@app.route('/rearcamera/all', methods=["GET"])
def rearcamera_all():
    try:
        with db.connect() as conn:
            query = 'select * from RearCamera'
            result = conn.execute(query).fetchall()
            return json.dumps([dict(r) for r in result])

    except Exception as e:
        return "it broke " + str(e)


##It took me hours to realize this.
#You MUST explicitly commit your transaction when trying to call a stored procedure or really doing anything other than selecting
# Do not make the same mistakes that I have 
# BTW all you need to do is wrap your .execute in trans = conn.begin() and then after, trans.commit()
@app.route('/deleteVehicle/<unitNumber>', methods=["DELETE"])
def deleteVehicle(unitNumber):
    try:
        with db.connect() as conn:
            trans = conn.begin()
            query = 'CALL deleteVehicle(' + unitNumber + ')'
            result = conn.execute(query)
            trans.commit()
            returnString = "Vehicle " + unitNumber + " has been deleted"
            return returnString

    except Exception as e:
        return "it brokedead " + str(e)

#Insert vehicle
#Input: unitNumber, make, model, lastModifyDate, badBoysCaught
# Output: none
@app.route('/InsertVehicle', methods=['POST'])
def InsertVehicle():
    ##get the parameters
    with db.connect() as conn:
        try: 
            args = request.form
            unitNumber = args.get("unitNumber")
            make = args.get("make")
            model = args.get("model")
            lastModifyDate = args.get("lastModifyDate")
            badBoysCaught = args.get("badBoysCaught")
            trans = conn.begin()
            query = 'call AddVehicle( ' + unitNumber  + ', \'' + make + '\', \'' + model + '\',\'' + lastModifyDate +  '\',' + badBoysCaught + ')'
            conn.execute(query)
            trans.commit()
            return "Vehicle added"
        except Exception as e:
            return "it broke " + str(e)

#Update Vehicle
# Input: Unit number along with any vehicle attribute you want to update
# Output: None
@app.route('/UpdateVehicle', methods=["PUT"])
def UpdateVehicle():
    with db.connect() as conn:
        try:
            args = request.form
            unitNumber = args.get("unitNumber")
            if unitNumber is None:
                return "unitNumber cannot be null"
            make = args.get("make")
            model = args.get("model")
            lastModifyDate = args.get("lastModifyDate")
            badBoysCaught = args.get("badBoysCaught")
            trans = conn.begin()
            if make is not None: 
                query = 'update Vehicle set make = \'' + make + '\' where unitNumber = ' + unitNumber
                conn.execute(query)
            if model is not None:
                query = 'update Vehicle set model = \'' + model + '\' where unitNumber = ' + unitNumber
                conn.execute(query)
            if lastModifyDate is not None:
                #This is a stored procedure since we need to convert the lastModify date string into a datetime object before the update
                query = 'call UpdateModifyDate( ' + unitNumber + ' , \'' + lastModifyDate + '\')'
                conn.execute(query)
            if badBoysCaught is not None:
                query = 'update Vehicle set badBoysCaught = \'' + badBoysCaught + '\' where unitNumber = ' + unitNumber
                conn.execute(query)
            trans.commit()
            return "Vehicle Updated"

        except Exception as e:
            return "It broke " + str(e)        

if __name__=='__main__':
    app.run(debug=True)