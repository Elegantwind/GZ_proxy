webpackJsonp([2],{"2uDm":function(t,e,l){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=l("P9l9"),o={data:function(){return{tableData:[]}},created:function(){var t=this;this.$http.get(n.h).then(function(t){return t.json()}).then(function(e){console.log(e.Response),t.tableData=e.Response})},methods:{toggleSelection:function(t){var e=this;t?t.forEach(function(t){e.$refs.multipleTable.toggleRowSelection(t)}):this.$refs.multipleTable.clearSelection()},handleSelectionChange:function(t){this.multipleSelection=t}}},a={render:function(){var t=this,e=t.$createElement,l=t._self._c||e;return l("div",[l("el-table",{ref:"multipleTable",staticStyle:{width:"100%"},attrs:{data:t.tableData,"tooltip-effect":"dark"},on:{"selection-change":t.handleSelectionChange}},[l("el-table-column",{attrs:{type:"selection",width:"55"}}),t._v(" "),l("el-table-column",{attrs:{prop:"function",label:"方法",width:"10"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v(t._s(e.row.function))]}}])}),t._v(" "),l("el-table-column",{attrs:{prop:"id",label:"id",width:"10"}}),t._v(" "),l("el-table-column",{attrs:{prop:"type",label:"地址","show-overflow-tooltip":""}})],1),t._v(" "),l("div",{staticStyle:{"margin-top":"20px"}},[l("el-button",{on:{click:function(e){t.toggleSelection([t.tableData[1],t.tableData[2]])}}},[t._v("切换第二、第三行的选中状态")]),t._v(" "),l("el-button",{on:{click:function(e){t.toggleSelection()}}},[t._v("取消选择")])],1)],1)},staticRenderFns:[]},i=l("VU/8")(o,a,!1,null,null,null);e.default=i.exports}});
//# sourceMappingURL=2.e585686f8cc2ec863bd1.js.map