/**
 * Created by Parteek Khushdil on 23-08-2017.
 */
(function () {
    myApp.config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/views/login.html',
                controller: 'loginController'
            })
            .when('/register', {
                templateUrl: '/static/views/register.html',
                controller: 'registerController'
            })
            .when('/home', {
                templateUrl: '/static/views/home.html',
                controller: 'homeController'
            })
            .otherwise({ redirectTo: '/' });
    });
})();
