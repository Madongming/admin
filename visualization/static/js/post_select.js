(function($){
    $.extend({
        StampTime: {
            CurTime: function(){
                return Date.parse(new Date());
            },
            DateToUnix: function(string) {
                var f = string.split(' ', 2);
                var d = (f[0] ? f[0] : '').split('-', 3);
                var t = (f[1] ? f[1] : '').split(':', 3);
                return (new Date(
                        parseInt(d[0], 10) || null,
                        (parseInt(d[1], 10) || 1) - 1,
                        parseInt(d[2], 10) || null,
                        parseInt(t[0], 10) || null,
                        parseInt(t[1], 10) || null,
                        parseInt(t[2], 10) || null
                        )).getTime();
            },
            UnixToDate: function(unixTime, isFull, timeZone) {
                if (typeof (timeZone) == 'number')
                {
                    unixTime = parseInt(unixTime) + parseInt(timeZone) * 60 * 60;
                }
                var time = new Date(unixTime * 1000);
                var ymdhis = "";
                ymdhis += time.getUTCFullYear() + "-";
                ymdhis += (time.getUTCMonth()+1) + "-";
                ymdhis += time.getUTCDate();
                if (isFull === true)
                {
                    ymdhis += " " + time.getUTCHours() + ":";
                    ymdhis += time.getUTCMinutes() + ":";
                    ymdhis += time.getUTCSeconds();
                }
                return ymdhis;
            }
        }
    });
})(jQuery);
$(document).ready(function(){
    $(".monitor_name").click(function(){
        if ($("input#time_start").val() === "" || $("input#time_end").val() === ""){
            alert("先选择时间段");
            return;
        }
        var data = {
            "time_start":$.StampTime.DateToUnix($("input#time_start").val()),
            "time_end": $.StampTime.DateToUnix($("input#time_end").val()),
            "monitor_name": $(this).text(),
            "interval": $("#interval option:selected").val()
        };
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/api/post_profile_data",
            "data": data,
            "success": function(result) {
                $('#container').show();
                eval("$('#container').highcharts("+JSON.parse(result)+")");
            }
        });
    });
});
