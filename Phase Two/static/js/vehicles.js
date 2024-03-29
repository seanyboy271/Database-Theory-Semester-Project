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
            if (data === 'You do not have permission to complete this action') {
                alert('You do not have permission to do this.');
            } else {
                alert("Successfully inserted Vehicle");
                window.location.href = "/vehicle/" + unitNumber
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert(errorThrown);
        }
    });
}