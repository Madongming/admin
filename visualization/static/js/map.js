$(function(){
    $("area").each(function(){
		var $x=-70;
		var $y=-80;	
		var name=$(this).attr("alt");	
        var city_id=$(this).attr("id");
		$(this).mouseover(function(e){
            var index_num=$(this).index();
			var dom="<div class='mapDiv'><p>提示消息<span class='name'></span><span class='num'></span></p></div>";
			$("body").append(dom);
			$(".name").text(name);
//	$(".num").text(index_num)
			$(".mapDiv").css({
                top: (e.pageY + $y)+"px",
				left: (e.pageX + $x)+"px"
			}).show("fast");
        }).mouseout(function(){
            $(".mapDiv").remove();
        }).mousemove(function(e){
            $(".mapDiv").css({
                top: (e.pageY + $y)+"px",
                left: (e.pageX + $x)+"px"
            })
        });
	});		   
});
