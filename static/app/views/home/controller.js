app.controller('homeController', function($scope, $state, $http) {
  $scope.items = [];
  $scope.showResolved = false;
  $http.get('/item', {params:{}}).
		then(function(response) {
				$scope.items = response.data.item;
				console.log($scope.items);
		});
});

app.filter('split', function() {
  return function(input, splitChar, splitIndex) {
    return input.split(splitChar)[splitIndex];
  }
});