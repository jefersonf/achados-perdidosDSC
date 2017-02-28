app.controller('homeController', function($scope, $state, $http) {
  $scope.items = [];
  $http.get('/item', {params:{}}).
		then(function(response) {
				$scope.items = response.data.item;
		});
});
