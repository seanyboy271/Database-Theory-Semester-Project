function CommonDetailViewModel() {
    self = this;

    self.VehicleWithRecentlyUploaded = ko.observable("Loading...");
    self.NewestArbitratorVersionVehicle = ko.observable("Loading...");
    self.VehcleWithOldestInpectionDate = ko.observable("Loading...");
    self.ITComputers = ko.observable("Loading...");
    self.VehiclesWithFrontAndRearCamera = ko.observable("Loading...");
    self.VehiclesWithKeyboardAndNoComputer = ko.observable("Loading...");
    self.ArbitratorWithBadStatusCodes = ko.observable("Loading...");
    self.VehiclesWithShortDockStands = ko.observable("Loading...");
    self.VehiclesWithTallDockStands = ko.observable("Loading...");




    self.getVehicleWithRecentlUploaded = function() {
        $.ajax({
            dataType: "json",
            url: '/VehicleWithRecentlyUploaded',
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    self.VehicleWithRecentlyUploaded(data[0].unitNumber);
                } else {
                    self.VehicleWithRecentlyUploaded("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getNewestArbitratorVersionVehicle = function() {
        $.ajax({
            dataType: "json",
            url: '/NewestArbitratorVersionVehicle',
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    self.NewestArbitratorVersionVehicle(data[0].unitNumber);
                } else {
                    self.NewestArbitratorVersionVehicle("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };


    self.getVehcleWithOldestInpectionDate = function() {
        $.ajax({
            dataType: "json",
            url: '/VehcleWithOldestInpectionDate',
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    self.VehcleWithOldestInpectionDate(data[0].unitNumber);
                } else {
                    self.VehcleWithOldestInpectionDate("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };


    self.getITComputers = function() {
        $.ajax({
            dataType: "json",
            url: '/ITComputers',
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    self.ITComputers(data[0]["Number of Computers"]);
                } else {
                    self.ITComputers("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };


    self.getVehiclesWithFrontAndRearCamera = function() {
        $.ajax({
            dataType: "json",
            url: '/VehiclesWithFrontAndRearCamera',
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    data = data[0]
                    self.VehiclesWithFrontAndRearCamera(data['Number of Vehicles']);
                } else {
                    self.VehiclesWithFrontAndRearCamera("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };


    self.getVehiclesWithKeyboardAndNoComputer = function() {
        $.ajax({
            dataType: "json",
            url: '/VehiclesWithKeyboardAndNoComputer',
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    self.VehiclesWithKeyboardAndNoComputer(data);
                } else {
                    self.VehiclesWithKeyboardAndNoComputer("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };


    self.getArbitratorWithBadStatusCodes = function() {
        $.ajax({
            dataType: "json",
            url: '/ArbitratorWithBadStatusCodes',
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    self.ArbitratorWithBadStatusCodes(data);
                } else {
                    self.ArbitratorWithBadStatusCodes("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getVehiclesWithShortDockStands = function() {
        $.ajax({
            dataType: "json",
            url: '/VehiclesWithDockType?dockType=short',
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    self.VehiclesWithShortDockStands(data);
                } else {
                    self.VehiclesWithShortDockStands("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getVehiclesWithTallDockStands = function() {
        $.ajax({
            dataType: "json",
            url: '/VehiclesWithDockType?dockType=tall',
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    self.VehiclesWithTallDockStands(data);
                } else {
                    self.VehiclesWithTallDockStands("N/A");
                }

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };


    self.getITComputers();
    self.getNewestArbitratorVersionVehicle();
    self.getVehcleWithOldestInpectionDate();
    self.getVehicleWithRecentlUploaded();
    self.getVehiclesWithFrontAndRearCamera();
    self.getVehiclesWithKeyboardAndNoComputer();
    self.getArbitratorWithBadStatusCodes();
    self.getVehiclesWithShortDockStands();
    self.getVehiclesWithTallDockStands();

    return self;
}

ko.applyBindings(new CommonDetailViewModel());