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
        var data = {
            "monitor_name": $(this).text(),
        };
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/api/post_get_profile_data",
            "data": data,
            "success": function(result) {
                $(".main_window").empty();
                var form_start = "<form id='pic_modify'>";
                var label_id = "<label for='id'>ID: </label>";
                var label_id_value = "<label id='id'>"+result.id+"</label><br />";
                var label_monitor_name = "<label for='monitor_name'>监控图表名称: </label>";
                var input_monitor_name = "<input type='text' id='monitor_name' value="+"'"+result.monitor_name+"'"+" /><br />";
                var label_index = "<label for='index'>查询索引: </label>";
                var input_index = "<input type='text' id='index' value="+"'"+result.index+"'"+" /><br />";
                var label_query = "<label for='query'>查询语句: </label>";
                var input_query = "<input type='text' id='query' value="+"'"+result.query+"'"+" /><br />";
                var label_fields = "<label for='fields'>查询字段（多）: </label>";
                var input_fields = "<input type='text' id='fields' value="+"'"+result.fields+"'"+" /><br />";
                var label_field = "<label for='field'>查询字段（单）: </label>";
                var input_field = "<input type='text' id='field' value="+"'"+result.field+"'"+" /><br />";
                var label_name = "<label for='name'>求和名称: </label>";
                var input_name = "<input type='text' id='name' value="+"'"+result.name+"'"+" /><br />";
                var label_size = "<label for='size'>TOP榜长度: </label>";
                var input_size = "<input type='text' id='size' value="+"'"+result.size+"'"+" /><br />";
                var label_sub_fields = "<label for='sub_fields'>子查询字段: </label>";
                var input_sub_fields = "<input type='text' id='sub_fields' value="+"'"+result.sub_fields+"'"+" /><br />";
                var label_mothod_type = "<label for='mothod_type'>查询方法: </label>";
                var input_mothod_type = "<select id='mothod_type'><option value='gen' id='gen'>gen</option><option value='per_sum' id='per_sum'>per_sum</option><option value='sum' id='sum'>sum</option><option value='cardinality' id='cardinality'>cardinality</option><option value='count' id='count'>count</option><option value='some_top' id='some_top'>some_top</option><option value='sub_query' id='sub_query'>sub_query</option><option value='sub_sum' id='sub_query'>sub_sum</option></select><br />";
                var label_pic_type = "<label for='pic_type'>监控图表类型: </label>";
                var input_pic_type = "<select id='pic_type'><option value='line'>line</option><option value='column'>column</option><option value='spline'>spline</option></select><br />";
                var input_submit = "<input type='button' value='提交'/>"
                var form_end = "</form>";
                $(".main_window").append(form_start, label_id, label_id_value, label_monitor_name,  input_monitor_name, label_index, input_index, label_query, input_query, label_fields, input_fields, label_field, input_field, label_name, input_name, label_size, input_size, label_sub_fields, input_sub_fields, label_mothod_type, input_mothod_type, label_pic_type, input_pic_type, input_submit, form_end);
                $("select#mothod_type").find("#"+result.mothod_type).attr("selected","selected");
                $("select#pic_type").find("#"+result.pic_type).attr("selected","selected");
                var update_data = {
                    "id":$("#id").text(),
                    "monitor_name":$("#monitor_name").val(),
                    "index":$("#index").val(),
                    "query":$("#query").val(),
                    "fields":$("#fields").val(),
                    "field":$("#field").val(),
                    "name":$("#name").val(),
                    "size":$("#size").val(),
                    "sub_fields":$("#sub_fields").val(),
                    "mothod_type":$("#mothod_type").val(),
                    "pic_type":$("#pic_type").val()
                };
                $("input:button").click(function(){
                    $.ajax({
                        "type": "POST",
            		    "dataType": "json",
            		    "url": "/api/post_update_pic_profile",
            		    "data": update_data,
                        "success": function(result) {
                            alert(result);
                        }
                    });
                });
            }
        });
    });
});
