$(function(){
    $("area").each(function(){
		var $x=-70;
		var $y=-80;	
		var name=$(this).attr("alt");	
        var city_id=$(this).attr("id");
		$(this).mouseover(function(e){
            var index_num=$(this).index();
            var data = {
                'city_id':city_id
            };
            $.ajax({
                "type": "POST",
                "dataType": "json",
                "url": "/api/post_get_city_data",
                "data": data,
                "success": function(result) {
			        var dom="<div class='mapDiv'><p>"+"交易量为"+result.data+"&nbsp&nbsp<span class='name'></span><span class='num'></span></p></div>";
			        $("body").append(dom);
			        $(".name").text(name);
			        $(".mapDiv").css({
                        top: (e.pageY + $y)+"px",
				        left: (e.pageX + $x)+"px"
			        }).show("fast");
                }
            });
        }).mouseout(function(){
            $(".mapDiv").remove();
        }).mousemove(function(e){
            $(".mapDiv").css({
                top: (e.pageY + $y)+"px",
                left: (e.pageX + $x)+"px"
            });
        });
        $(this).click(function(){
            var data_pic = {
                "time_start":Date.parse(new Date()) - 60 * 60 * 24 * 7 * 1000,
                "time_end": Date.parse(new Date()),
                "city_id": city_id,
                "interval": '24h'
            };
            $.ajax({
                "type": "POST",
                "dataType": "json",
                "url": "/api/post_get_order_countAndmoney_data",
                "data": data_pic,
                "success": function(result) {
                    $('#container_order').show();
                    eval("$('#container_order').highcharts("+JSON.parse(result)+")");
                }
            });
            $.ajax({
                "type": "POST",
                "dataType": "json",
                "url": "/api/post_get_site_DAUPV_data",
                "data": data_pic,
                "success": function(result) {
                    $('#container_daupv').show();
                    eval("$('#container_daupv').highcharts("+JSON.parse(result)+")");
                }
            });
        });
    });		   
});
