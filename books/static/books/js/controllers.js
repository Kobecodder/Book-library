'use strict';

/* Controllers */

photoGallery.controller('galleryController', function($scope, apiGallery, Pagination, $routeParams){
    var rest_data;
    var archive_id = $routeParams.archive_id || "";
    rest_data = apiGallery.getGallery(archive_id);
    rest_data.then(
        function(success){
            $scope.response_data = success.response_data;
            $scope.pagination = Pagination.getNew(4);
            $scope.pagination.numPages = Math.ceil($scope.response_data.length/$scope.pagination.perPage);

        },
        function(response){
            console.log(response);
        }
    );

});
