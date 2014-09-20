(function() {
    var outbox = new ReconnectingWebSocket("ws://"+ location.host + "/vote");

    outbox.onclose = function(h) {
        console.log('outbox closed ' + h.reason + ' code ' + h.code);
        this.outbox = new WebSocket(outbox.url);
    };

  var _name = 'incognito';
  var signin = function() {
    _name = $('#signin-input')[0].value || _name;

    $('#signin-container').animate({'height': '0%'}, 500);
    $('#control-container').animate({'height': '100%'}, 500);
    $('#mascot').animate({'bottom': '-1000'}, 500);
    $('#left-button, #right-button').show();

    return false;
  };

  var vote = function(direction, name) {
      outbox.send(JSON.stringify({ side: direction, name: name }));
  };

  $('#signin-form button').on('click', signin);
  $('#signin-form').on('submit', signin);

  $('#left-button, #right-button').on('click', function() {
    var direction = $(this).data('direction');
    vote(direction, _name);

    $('#'+direction+'-arrow')
      .fadeIn()
      .animate({'top': '120%', 'opacity': 0})
      .fadeOut()
      .animate({'top': '25%', 'opacity': 1})
      ;
  });

  // Preloading like is 1999
  var images = [];
  var imageSrcs = ['/static/img/keypad.jpg', '/static/img/arrow_left.png', '/static/img/arrow_right.png'];
  imageSrcs.forEach(function() {
    images[arguments[1]] = new Image();
    images[arguments[1]].src = arguments[0];
  });


//fake voting
// setInterval(function() {vote('left', 'Griselda')}, 900);
// setInterval(function() {vote('right', 'Hugolina')}, 1500);
// setInterval(function() {vote('right', 'Walter Junior')}, 2500);

})();
