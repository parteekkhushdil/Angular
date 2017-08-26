/**
 * Created by Parteek Khushdil on 23-08-2017.
 */
myApp.controller('registerController', ['$scope', '$log', '$http',
    function ($scope, $log, $http) {
        $scope.submit = function () {
            $http.post('/ajax/', {
                'method': 'register_user',
                'data': {
                    'firstName': $scope.firstName,
                    'lastName': $scope.lastName,
                    'username': $scope.userName,
                    'password': $scope.password,
                }
            }).then(function (response) {

            });
            $log.log($scope.firstName, $scope.lastName, $scope.userName, $scope.password);
        }
    }]);
