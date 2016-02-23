(function() {
  var db = {
    loadData: function(filter) {
      var data = {"data": JSON.stringify(filter)}
      return $.ajax({
        type: "GET",
        url: "config",
        data: data,
        dataType: "json",
        success: function(result) {
          console.log(result);
        }
      });
    },
    insertItem: function(item) {
      var data = {"data": JSON.stringify(item)}
      return $.ajax({
        type: "POST",
        url: "config",
        data: data,
        dataType: "json",
        success: function(result) {
          console.log(result);
        }
      });
    },
    updateItem: function(item) {
      var data = {"data": JSON.stringify(item)}
      return $.ajax({
        type: "PUT",
        url: "config",
        data: data,
        dataType: "json",
        success: function(result) {
          console.log(result);
        }
      });
    },
    deleteItem: function(item) {
      var data = {"data": JSON.stringify(item)}
      return $.ajax({
        type: "DELETE",
        url: "config" + '?' + $.param(data),
        dataType: "json",
        success: function(result) {
          console.log(result);
        }
      });
    }
  };
  window.db = db;
}());
