function VehicleViewModel() {
    self = this;

    self.vehicles = ko.observableArray([]);

    self.getVehicles = function () {
        $.ajax({
            dataType: "json",
            url: '/vehicle/all',
            success: function (data, textStatus, XmlHttpRequest) {
                console.log(data);
                self.vehicles(data);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getVehicles();

    return self;
}

ko.applyBindings(new VehicleViewModel());


function InsertVehicle() {
    let unitNumber = document.getElementById('unitNumber').value
    let make = document.getElementById('make').value
    let model = document.getElementById('model').value
    let lastModDate = document.getElementById('lastModDate').value
    let badBoys = document.getElementById('BadBoysCaught').value

    let formData = { unitNumber: unitNumber, make: make, model: model, lastModDate: lastModDate, badBoys: badBoys }
    console.log(formData)

    $.ajax({
        type: "post",
        data: formData,
        url: '/InsertVehicle',
        success: function (data, textStatus, XmlHttpRequest) {
            alert("Successfully inserted Vehicle");
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown);
        }
    });
}