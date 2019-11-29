function MobileComputerDetailViewModel(res) {
    self = this;

    self.computer = ko.observable(JSON.parse(res)[0]);
    console.log(self.computer());
    self.cableColor = ko.observable("Loading...");

    self.getCableColor = function() {
        // $.ajax({
        //     dataType: "json",
        //     url: '/CradlepointCableColor?unitNumber=' + self.vehicle().unitNumber,
        //     success: function (data, textStatus, XmlHttpRequest) {
        //         if (data.length > 0 && 'cableColor' in data[0]) {
        //             self.cableColor(data[0].cableColor);
        //         } else {
        //             self.cableColor("N/A");
        //         }
        //
        //     },
        //     error: function (XMLHttpRequest, textStatus, errorThrown) {
        //         alert(errorThrown);
        //     }
        // });
    };

    self.getCableColor();

    return self;
}