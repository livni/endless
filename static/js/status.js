(function() {
  var fetchData = function() {
    $.ajax({
      type: 'GET',
      url: '/get-status',
      success: refreshDisplay,
      error: function() {},
      cache:false
    });
    setTimeout(fetchData, 200);
  };

  var refreshDisplay = function(data) {
    var leftHeight = Math.floor((data.left.length / data['action-limit'])*100)+'%';
    var rightHeight = Math.floor((data.right.length / data['action-limit'])*100)+'%';
    $('#tube-left .fill').animate({height: leftHeight}, 200);
    $('#tube-right .fill').animate({height: rightHeight}, 200);

    var mascotRotate = (data.right.length - data.left.length) / data['action-limit'];
    $('#mascot').css({transformOriginX:'50%', transformOriginY:'100%', left: ($(window).width()/2-166)}).animate({rotate: mascotRotate*3}, 400);
  };

  fetchData();
})();