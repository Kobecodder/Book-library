'use strict';


function templateLoader(template_name) {
    var template_prefix = 'templates/';
    return template_prefix + template_name
}
// Declare app level module which depends on filters, and services
var photoGallery = angular.module('angallery', ['ngResource','SimplePagination']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: templateLoader('gallerylist'),
                controller: 'galleryController'
            })
            .when('/books/:archive_id', {
                templateUrl: templateLoader('gallerydetail'),
                controller: 'galleryController'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);