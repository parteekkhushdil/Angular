/**
 * Created by Parteek Khushdil on 23-08-2017.
 */
(function () {
    myApp.config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/views/main.html',
                controller: 'mainController'
            })
            .when('/second', {
                templateUrl: '/static/views/second.html',
                controller: 'secondController'
            })
    });
})();
