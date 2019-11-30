function ArbitratorsViewModel() {
    self = this;

    self.arbitrators = ko.observableArray([]);

    self.getList = function () {
        $.ajax({
            dataType: "json",
            url: '/arbitrator/all',
            success: function (data, textStatus, XmlHttpRequest) {
                console.log(data);
                self.arbitrators(data);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getList();

    return self;
}

ko.applyBindings(new ArbitratorsViewModel());