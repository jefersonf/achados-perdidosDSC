app.controller('homeController', function($scope, $state, $http) {
  $scope.items = [];
  $scope.addItemForm = {};
  $http.get('/item', {params:{}}).
		then(function(response) {
				$scope.items = response.data.item;
		});
});
