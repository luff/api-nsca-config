$(function() {
  $("#jsGrid").jsGrid({
    width: "100%",

    filtering: false,
    editing: true,
    sorting: true,
    paging: true,
    autoload: true,

    pageSize: 15,
    pageButtonCount: 5,

    controller: db,

    fields: [
      {
        name: "H",
        type: "text",
        title: "主机地址",
        editing: false,
        width: 50
      },
      {
        name: "N",
        type: "text",
        title: "监控名称",
        editing: false,
        width: 80
      },
      {
        name: "I",
        type: "number",
        title: "检测间隔(分)",
        width: 40
      },
      {
        name: "A",
        type: "number",
        title: "触发尝试(次)",
        width: 40
      },
      {
        name: "w",
        type: "number",
        title: "警告值(w)",
        width: 35
      },
      {
        name: "c",
        type: "number",
        title: "临界值(c)",
        width: 35
      },
      {
        type: "control",
        modeSwitchButton: false,
        editButton: false
      }
    ]
  });

  $(".config-panel input[type=checkbox]").on("click", function() {
    var $cb = $(this);
    $("#jsGrid").jsGrid("option", $cb.attr("id"), $cb.is(":checked"));
  });
});
