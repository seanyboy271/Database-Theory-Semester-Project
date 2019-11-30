function ListViewModel() {
    self = this;

    self.cameras = ko.observableArray([]);

    self.getList = function () {
        $.ajax({
            dataType: "json",
            url: '/frontcamera/all',
            success: function (data, textStatus, XmlHttpRequest) {
                console.log(data);
                self.cameras(data);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getList();

    return self;
}

ko.applyBindings(new ListViewModel());