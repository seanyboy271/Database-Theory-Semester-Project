function MobileComputerDocksViewModel() {
    self = this;

    self.docks = ko.observableArray([]);

    self.getMobileComputers = function () {
        $.ajax({
            dataType: "json",
            url: '/mobilecomputerdock/all',
            success: function (data, textStatus, XmlHttpRequest) {
                console.log(data);
                self.docks(data);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getMobileComputers();

    return self;
}

ko.applyBindings(new MobileComputerDocksViewModel());