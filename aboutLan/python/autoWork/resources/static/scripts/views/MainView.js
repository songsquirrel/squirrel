$ns("${faceId}.views");
//component_import

test.views.MainView = function () {
    var me = $extend(mx.views.View);
    var base = {};

    base.init = me.init;
    me.init = function () {
        base.init();
        _initControls();
    };

    function _initControls() {
        //component_invoke

        //component_show
        me.on("activate", me.controller._onactivate);
    }
    //component_init   

    return me.endOfClass(arguments);
};