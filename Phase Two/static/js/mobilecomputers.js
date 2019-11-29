function MobileComputerViewModel() {
    self = this;

    self.computers = ko.observableArray([]);

    self.getMobileComputers = function () {
        $.ajax({
            dataType: "json",
            url: '/mobilecomputer/all',
            success: function (data, textStatus, XmlHttpRequest) {
                console.log(data);
                self.computers(data);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getMobileComputers();

    return self;
}

ko.applyBindings(new MobileComputerViewModel());