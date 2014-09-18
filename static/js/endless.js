(function() {
  var _name = 'incognito';
  var signin = function() {
    _name = $('#signin-input')[0].value || _name;
    window.console.log(_name);
    return false;
  };

  $('#signin-form button').on('click', signin);
  $('#signin-form').on('submit', signin);
})();