'use strict'

angular.module('app', ['ui.router', 'app.views'])
.config(['$stateProvider', '$urlRouterProvider',
  ($stateProvider, $urlRouterProvider) ->

    $urlRouterProvider.otherwise '/'
  
    $stateProvider
    .state('app',
      url: '/'
      # template: 'Hi'
      templateUrl: 'module1/detail.html'
      controller: ['$scope', ($scope) ->
        $scope.APP_NAME = 'foo'
      ]
    )
  ])
