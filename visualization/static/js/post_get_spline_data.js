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
        "url": "/api/post_get_source_data",
        "data": data,
        "success": function(results) {
            result = 
            return ;
        }    
    });
};

var time_start = Date.parse(new Date()) - 5000;
var time_end = Date.parse(new Date());
var monitor_name = "{{ monitor_names.1 }}";
var interval = '5s'
