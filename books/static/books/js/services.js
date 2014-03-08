'use strict';

/* Services */

photoGallery.factory('apiGallery', function($resource, $q){
    var ResourceKeyspace = $resource('/books/api/books/:archive_id', {archive_id: '@archive_id'});

    return {getGallery: function(archive_id ) {
            var deferred = $q.defer();
            ResourceKeyspace.get({archive_id: archive_id },
                function (success) {
                    deferred.resolve(success);
                },
                function (error) {
                    setTimeout(function(){
                        ResourceKeyspace.get({archive_id: archive_id },
                            function (success) {
                                deferred.resolve(success);
                            },
                            function (error) {
                                deferred.reject(error);
                            });
                    }, 1000);

                });
            return deferred.promise;
        }
    }
});

