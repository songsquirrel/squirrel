/**
 * 初始化DataGrid
 */
function _initDataGrid (){
        // TODO 设置后台路径
		var restUrl = "";
		/* 初始化 EntityContainer */
		var gridEntityContainer = new mx.datacontainers.GridEntityContainer({
			baseUrl : ${fileName}.mappath(restUrl),
			iscID : "-1", // iscID 是数据元素的统一权限功能编码。默认值为 "-1"
			// ，表示不应用权限设置。
			loadMeta : false,
			primaryKey : "objId"
		});
		/**
		 * 计划展示表格
		 */
		me.dataGrid = new mx.datacontrols.DataGrid({
            /*
            {
                name : "jhbh",
                caption : "计划编号 ",
                width : "170px",
                editorType : "TextEditor",
                renderCell : function(item, cell) {
                    cell.text(item.getValue("jhbh"));
                    cell[0].style.cursor = "pointer";
                    cell[0].style.color = "blue";
                    cell[0].style.textAlign = "center";
                    cell[0].style.textDecoration = "underline";

                    cell.click(function() {
                        me.controller._jxjhDetail(item.values);
                    })
                }
            }, {
                name : "jhlx",
                caption : "计划类型 ",
                editorType : "DropDownEditor",
                ondropdown : me.controller.
            }, {
                name : "jhtdkssj",
                caption : "计划停电开始时间 ",
                editorType : "DateTimeEditor",
                formatString : "yyyy-MM-dd HH:mm"
			}
            */
			columns : [${columnName}],
			// 构造列排序条件，如果有多列，则以逗号分隔。例sorter: "school ASC, class DESC"
			sorter : "tbsj desc",
			enableCellTip : true,
			displayCheckBox : true,
			displayRowNumber : true,
			displayPrimaryKey : false,// 列表是否显示主键
			allowEditing : false, // 列表默认不可编辑
			pageSize : 20,
			pageSizeOptions : [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ],
			entityContainer : gridEntityContainer
		});
		me.dataGrid.on("load", me.controller.dataGrid_onload);
}