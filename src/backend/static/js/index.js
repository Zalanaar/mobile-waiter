var app = angular.module("app", []);
var address = 'http://127.0.0.1:5000'

app.controller("AppCtrl", function ($scope, $http, $window) {

    $scope.signIn = function (authToken) {
        console.log(authToken);
        $http.post('${address}/signIn', authToken).then(function (response) {

            if(response.data.e == 0) {
                $window.location.href = '${address}/v1';
            }else {
                alert("access denied")
            }
        });
    };

    $scope.signUp = function (reg) {
        console.log(reg);
        $http.post('${address}/signUp', reg).then(function (response) {
            console.log("Sign up success");
        })

    }
});