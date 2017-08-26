/**
 * Created by Parteek Khushdil on 25-08-2017.
 */

myApp.controller('homeController', ['$scope', '$http', function ($scope, $http) {

    console.log('home controller');
    $http.post('/ajax/', {
        'method': 'get_all_users',
    }).then(function (response) {
        console.log(response);
        if (response.data) {
            $scope.users = response.data;
        }
    });

}]);