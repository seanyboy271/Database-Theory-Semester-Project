function CradlepointsViewModel() {
    self = this;

    self.cradlepoints = ko.observableArray([]);

    self.getList = function () {
        $.ajax({
            dataType: "json",
            url: '/cradlepoint/all',
            success: function (data, textStatus, XmlHttpRequest) {
                console.log(data);
                self.cradlepoints(data);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getList();

    return self;
}

ko.applyBindings(new CradlepointsViewModel());