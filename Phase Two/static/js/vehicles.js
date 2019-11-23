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