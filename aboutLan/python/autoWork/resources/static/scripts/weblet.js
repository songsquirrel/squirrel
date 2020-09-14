$import("${fileName}.views.MainViewController");

mx.weblets.WebletManager.register({
    id: "${fileName}",
    name: "",
    requires: [],
    onload: function(e)
    {
    },
    onstart: function(e)
    {
        var mvc = new ${fileName}.views.MainViewController();
        e.context.rootViewPort.setViewController(mvc);
    }
});