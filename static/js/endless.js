(function() {
  var _name = 'incognito';
  var signin = function() {
    _name = $('#signin-input')[0].value || _name;

    $('#signin-container').animate({'height': '0%'}, 500);
    $('#control-container').animate({'height': '100%'}, 500);
    $('#left-button, #right-button').show();

    return false;
  };

  $('#signin-form button').on('click', signin);
  $('#signin-form').on('submit', signin);

  $('#left-button, #right-button').on('click', function() {
    var direction = $(this).data('direction');
    $.ajax({
        type: 'GET',
        url: '/vote',
        data: {"side": direction, "name": _name},
        success: function() {},
        error: function() {},
        cache:false
    });

  });

  // Preloading like is 1999
  var imagePhone = new Image();
  imagePhone = '/static/img/keypad.jpg';
})();
