function VehicleDetailViewModel(res) {
    self = this;

    self.vehicle = ko.observable(JSON.parse(res)[0]);
    self.cableColor = ko.observable("Loading...");
    self.pcName = ko.observable("Loading...");
    self.cradlepointCardNumber = ko.observable("Loading...");

    self.getCableColor = function() {
        $.ajax({
            dataType: "json",
            url: '/CradlepointCableColor?unitNumber=' + self.vehicle().unitNumber,
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0 && 'cableColor' in data[0]) {
                    self.cableColor(data[0].cableColor);
                } else {
                    self.cableColor("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getPCName = function() {
        $.ajax({
            dataType: "json",
            url: '/PCNameInVehicle?unitNumber=' + self.vehicle().unitNumber,
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0 && 'PCName' in data[0]) {
                    self.pcName(data[0].PCName);
                } else {
                    self.pcName("N/A");
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getCradlepointCardNumber = function() {
        $.ajax({
            dataType: "json",
            url: '/CradlePointCardNumber?unitNumber=' + self.vehicle().unitNumber,
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0 && 'cardNumber' in data[0]) {
                    self.cradlepointCardNumber(data[0].cardNumber);
                } else {
                    self.cradlepointCardNumber("N/A");
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };



    self.getCableColor();
    self.getPCName();
    self.getCradlepointCardNumber();

    return self;
}

document.getElementById('deleteButton').onclick = function (){
        $.ajax({
            type: "delete",
            url: '/deleteVehicle/' + self.vehicle().unitNumber,
            success: function (data, textStatus, XmlHttpRequest) {
                alert("Vehicle Deleted")
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
}