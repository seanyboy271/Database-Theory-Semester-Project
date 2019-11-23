function VehicleViewModel() {
    self = this;

    self.vehicles = ko.observable('test');

    self.getVehicles = function() {
        $.ajax({
                dataType: "json",
                url: '/VehicleWithPC'
            })
            .done(function(response) {
                alert('done');
                self.vehicles(response);
            })
            .fail(function(response) {
                alert('Error:' + response);
            });
    };

    self.getVehicles();

    return self;
}

ko.applyBindings(new VehicleViewModel());