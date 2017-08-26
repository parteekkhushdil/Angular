/**
 * Created by Parteek Khushdil on 23-08-2017.
 */
myApp.controller('loginController', ['$scope', '$http', '$location', function ($scope, $http, $location) {

    console.log('login controller');
    $scope.submit = function () {
        $http.post('/ajax/', {
            'method': 'check_user_login',
            'data': {
                'username': $scope.userName,
                'password': $scope.password
            }
        }).then(function (response) {
            if (response.data) {
                 $location.path('/home')
            }
        });
    }
}]);