function KeyboardsViewModel() {
    self = this;

    self.keyboards = ko.observableArray([]);

    self.getList = function () {
        $.ajax({
            dataType: "json",
            url: '/keyboard/all',
            success: function (data, textStatus, XmlHttpRequest) {
                console.log(data);
                self.keyboards(data);
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
    };

    self.getList();

    return self;
}

ko.applyBindings(new KeyboardsViewModel());