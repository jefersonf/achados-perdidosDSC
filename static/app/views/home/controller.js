app.controller('homeController', function($scope, $state, $http) {
  $scope.items = [{title: "hello", description: "I am a nice object!"}, {title: "hello2", description: "I am a nice object!"}];

  $http.get('/item', {params:{}}).
		then(function(response) {
				$scope.items = response.data.item;
		});
});
[]
