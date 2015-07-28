/**
 * Created by liuzheng on 14-12-8.
 */
function HbaseList($scope, $http, ngTableParams) {
    $http({
        url: "/api/list",
        method: 'GET'
//        headers: {
//            "Authorization": Data.token()
//        },
//        data: {"uid": Data.uid()}
    }).success(function (data) {
        $scope.status = data["status"];//1 true or 0 false
        //Data.token = data["token"];
//        $scope.message = data["message"];
        $scope.data = data['data'];
        if ($scope.status) {
            //仅需要对message中的数据做处理
            $scope.list = $scope.data;
            $scope.weibo = [];
            $scope.tweibo = [];
            $scope.Data = [];
            for ( u in $scope.list['weibo']) {
                $scope.weibo.push({'id': u, 'status': $scope.list['weibo'][u]})
            }
            for (u in $scope.list['tweibo']) {
                $scope.tweibo.push({'id': u, 'status': $scope.list['tweibo'][u]})
            }
            $scope.Data = $scope.weibo;
            $scope.tableParams = new ngTableParams({
                page: 1,            // show first page
                count: 10           // count per page
            }, {
                total: $scope.Data.length, // length of data
                getData: function ($defer, params) {
                    $defer.resolve($scope.Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                }
            });
            $scope.dataswitch = function (target) {
                if (target == 'tweibo') {
                    $scope.Data = $scope.tweibo
                } else {
                    $scope.Data = $scope.weibo
                }
                $scope.tableParams = new ngTableParams({
                    page: 1,            // show first page
                    count: 10           // count per page
                }, {
                    total: $scope.Data.length, // length of data
                    getData: function ($defer, params) {
                        $defer.resolve($scope.Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                    }
                });
            }
        } else {
        }
    }).error(function (data) {
    });
}