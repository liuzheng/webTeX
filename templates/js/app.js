/**
 * Created by liuzheng on 14-12-8.
 */
'use strict';
/**
 * Created by liuzheng on 6/19/14.
 */
var NgApp = angular.module('NgApp', ['ngTable']);
NgApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
/*NgApp.config(['$routeProvider',
    function ($routeProvider, $rootScope) {

//        $routeProvider.
//            when('/', {
//                templateUrl: 'main.html',
//                controller: 'Indexx'
//            }).
//            when('/user', {
//                templateUrl: 'page.html',
//                controller: 'TestShow'
//            }).
//            when('/rock&roll/:rrid', {
//                templateUrl: 'page.html',
//                controller: 'RockRoll'
//            }).
//            when('/loginok', {
//                templateUrl: 'page.html',
//                controller: 'LoginOk'
//            }).
//            when('/test', {
//                templateUrl: 'page.html',
//                controller: 'TestPage'
//            }).
//            when('/test/:tid', {
//                templateUrl: 'page.html',
//                controller: 'TestPageTid'
//            }).
//            otherwise({
//                redirectTo: '/'
//            });
    }]);*/
/*NgApp.factory('Data', function (webStorage) {
    function _data() {
        this._flag = 0;
        this.flag = function () {
            if (this._flag == "" || this._flag == null) {
                this._flag = webStorage.get("flag");
                if (this._flag == "" || this._flag == null) {
                    this._flag = 0;
                    webStorage.add('flag', 0);
                }
            }
            return this._flag;
        };
        this.setFlag = function (to) {
            webStorage.remove('flag');
            webStorage.add('flag', to);
            this._flag = to;
        };

        this._key1 = "";
        this.key1 = function () {
            if (this._key1 == "" || this._key1 == null) {
                this._key1 = webStorage.get("key1");
            }
            return this._key1;
        };
        this.setKey1 = function (to) {
            webStorage.remove('key1');
            webStorage.add('key1', to);
            this._key1 = to;
        };
    }

    return new _data();
});
NgApp.run(function ($rootScope) {
    $rootScope.editorOptions = {
        language: 'zh-cn',
        uiColor: '#efefef',
        skin: 'kama',
        font_names: '宋体;黑体;楷体_GB2312;Arial;Comic Sans MS;Courier New;Tahoma;Times New Roman;Verdana'
    };
});*/
