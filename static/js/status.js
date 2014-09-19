function StatusCtrl($scope) {
    $scope.state = {};

    function refreshDisplay(state) {
        $scope.state = state;
        $scope.$apply();
    }

    var update = function() {
        $.ajax({
            type: 'GET',
            url: '/get-status',
            success: refreshDisplay,
            error: function() {},
            cache:false
        });
    };
    var interval = 200;
    setInterval (update, interval);
}

