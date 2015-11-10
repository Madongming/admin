(function($){
    $.extend({
        RefreshToUnix: function(string){
            var f = string.slice(-1);
            var d = string.slice(0, -1);
            if(f === 'm'){
                return parseInt(d) * 60 * 1000;
            }
            if(f === 's'){
                return parseInt(d) * 1000;
            }
        } 
    });
})(jQuery);

function dorefresh(time_start, time_end, monitor_names, interval, container){
    var data = {
        "time_start": time_start,
        "time_end": time_end,
        "monitor_name": monitor_names,
        "interval": interval
    };
    $.ajax({
        "type": "POST",
        "dataType": "json",
        "url": "/api/post_profile_data",
        "data": data,
        "success": function(result) {
            $('#container').show();
            eval(container+".highcharts("+JSON.parse(result)+")");
        }    
    });
};

$(document).ready(function(){
    dorefresh(Date.parse(new Date()) - $.RefreshToUnix($(".wrapper1>#lefttop>#time_before option:selected").val()), Date.parse(new Date()), "{{ monitor_names.1 }}", $(".wrapper1>#lefttop>#time_interval option:selected").val(), "$('#container1')");
    setInterval("dorefresh(Date.parse(new Date()) - $.RefreshToUnix($(\".wrapper1>#lefttop>#time_before option:selected\").val()), Date.parse(new Date()), \"{{ monitor_names.1 }}\", $(\".wrapper1>#lefttop>#time_interval option:selected\").val(), \"$('#container1')\")", $.RefreshToUnix($(".wrapper1>#lefttop>#time_refresh option:selected").val()));
});
