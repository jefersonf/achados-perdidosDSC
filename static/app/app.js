
var app = angular.module('app', ['ui.router', 'door3.css', 'ngCookies']);

app.config(function($stateProvider, $urlRouterProvider,  $cssProvider) {

    $urlRouterProvider.otherwise('/home');

    $stateProvider

        .state('home', {
            url: '/home',
            controller: 'homeController',
            templateUrl: '/app/views/home/template.html',
        })

});
