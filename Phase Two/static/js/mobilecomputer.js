function MobileComputerDetailViewModel(res) {
    self = this;

    self.computer = ko.observable(JSON.parse(res)[0]);
    console.log(self.computer());
    self.WindowsVersion = ko.observable("Loading...");
    self.GpsUpdateLastRun = ko.observable("Loading...");
    self.ArbitratorVersion = ko.observable("Loading...");

    self.getSoftwareStatus = function() {
        $.ajax({
            dataType: "json",
            url: '/softwarestatus/' + self.computer().serialNumber,
            success: function (data, textStatus, XmlHttpRequest) {
                if (data.length > 0) {
                    console.log(data[0]);
                    self.WindowsVersion(data[0].WindowsVersion);
                    self.GpsUpdateLastRun(data[0].GpsUpdateLastRun);
                    self.ArbitratorVersion(data[0].ArbitratorVersion);
                } else {
                    self.WindowsVersion("N/A");
                    self.GpsUpdateLastRun("N/A");
                    self.ArbitratorVersion("N/A");
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getSoftwareStatus();

    return self;
}