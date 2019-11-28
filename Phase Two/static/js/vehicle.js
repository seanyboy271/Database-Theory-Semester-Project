function VehicleDetailViewModel(res) {
    self = this;

    self.vehicle = ko.observable(JSON.parse(res));

    console.log(res);
    console.log(JSON.parse(res));
    console.log(self.vehicle);

    return self;
}