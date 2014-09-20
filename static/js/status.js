(function() {
  var fetchData = function() {
    $.ajax({
      type: 'GET',
      url: '/get-status',
      success: refreshDisplay,
      error: function() {},
      cache:false
    });
    setTimeout(fetchData, 750);
  };

  var refreshDisplay = function(data) {
    window.console.log(data);
    $('#leftVotes');
  };

  fetchData();
})();