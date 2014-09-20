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
    var position = ((data['current-position']-2)*250);
    var leftPos = ($(window).width()/2-166+position)+'px';
    $('#mascot').css({transformOriginX:'50%', transformOriginY:'100%'}).animate({rotate: mascotRotate, left: leftPos}, 200);
    var namesLeft = '';
    var namesRight = '';
    var votesLeft = {};
    var votesRight = {};
    data.left.forEach(function(name) {
      votesLeft[name] = votesLeft[name] ? votesLeft[name]+1 : 1;
      namesLeft += '<li class="'+name+'">'+name+'</li>';
    })
    for (name in votesLeft) {
    }
    data.right.forEach(function(name) {
      votesRight[name] = votesRight[name] ? votesRight[name]+1 : 1;
      namesRight += '<li class="'+name+'">'+name+'</li>';
    })
    for (name in votesRight) {
    }
    $('#tube-left ul').html(namesLeft);
    $('#tube-right ul').html(namesRight);
  };

  fetchData();
})();