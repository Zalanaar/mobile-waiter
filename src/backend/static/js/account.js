var app = angular.module("app", []);
var address = 'http://127.0.0.1:5000'


app.controller("AppCtrl", function ($scope, $http) {



    $http.get('${address}/client')
        .then(function (response) {
            $scope.client=response.data;
        });

    $http.get('${address}/menu')
        .then(function (response) {
            $scope.menu=response.data;
        });
    
    $scope.delete = function (id) {
        $http.get('${address}/menu/' + id + '/delete');
        $scope.menu.splice(id, 1);
        console.log("delete item with id = " + id);
    };

    $scope.addDish = function (newDish) {
        $http.post('${address}/menu/add', newDish).then(function (response) {
            console.log("new dish was added");
            var dish = angular.copy(newDish);
            $scope.menu.push(dish);
            $scope.newDish = null;
        })
    };
});