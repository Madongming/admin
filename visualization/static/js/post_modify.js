$(document).ready(function(){
    $("input:button").click(function(){
        $(".main_window").empty();
        var form_start = "<form id='pic_modify'>";
        var label_monitor_name = "<label for='monitor_name'>监控图表名称: </label>";
        var input_monitor_name = "<input type='text' id='monitor_name'/><br />";
        var label_index = "<label for='index'>查询索引: </label>";
        var input_index = "<input type='text' id='index'/><br />";
        var label_query = "<label for='query'>查询语句: </label>";
        var input_query = "<input type='text' id='query'/><br />";
        var label_fields = "<label for='fields'>查询字段（多）: </label>";
        var input_fields = "<input type='text' id='fields'/><br />";
        var label_field = "<label for='field'>查询字段（单）: </label>";
        var input_field = "<input type='text' id='field'/><br />";
        var label_name = "<label for='name'>求和名称: </label>";
        var input_name = "<input type='text' id='name'/><br />";
        var label_size = "<label for='size'>TOP榜长度: </label>";
        var input_size = "<input type='text' id='size'/><br />";
        var label_sub_fields = "<label for='sub_fields'>子查询字段: </label>";
        var input_sub_fields = "<input type='text' id='sub_fields'/><br />";
        var label_mothod_type = "<label for='mothod_type'>查询方法: </label>";
        var input_mothod_type = "<select id='mothod_type'><option value='gen' id='gen'>gen</option><option value='per_sum' id='per_sum'>per_sum</option><option value='sum' id='sum'>sum</option><option value='cardinality' id='cardinality'>cardinality</option><option value='count' id='count'>count</option><option value='some_top' id='some_top'>some_top</option><option value='sub_query' id='sub_query'>sub_query</option><option value='sub_sum' id='sub_query'>sub_sum</option></select><br />";
        var label_pic_type = "<label for='pic_type'>监控图表类型: </label>";
        var input_pic_type = "<select id='pic_type'><option value='line'>line</option><option value='column'>column</option><option value='spline'>spline</option></select><br />";
        var input_submit = "<input type='button' value='提交'/>"
        var form_end = "</form>";
        $(".main_window").append(form_start, label_monitor_name,  input_monitor_name, label_index, input_index, label_query, input_query, label_fields, input_fields, label_field, input_field, label_name, input_name, label_size, input_size, label_sub_fields, input_sub_fields, label_mothod_type, input_mothod_type, label_pic_type, input_pic_type, input_submit, form_end);
        $("input:button").click(function(){
            var create_data = {
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
            $.ajax({
                "type": "POST",
                "dataType": "json",
                "url": "/api/post_create_pic_profile",
                "data": create_data,
                "success": function(result) {
                    if (result){
                        alert('创建成功！');
                        window.location.href='/manage_pic';
                    }
                }
            });
        });        
    });

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
                var input_modify_submit = "<input type='button' id='modify_button' value='修改'/>"
                var input_delete_submit = "<input type='button' id='delete_button' value='删除'/>"
                var form_end = "</form>";
                $(".main_window").append(form_start, label_id, label_id_value, label_monitor_name,  input_monitor_name, label_index, input_index, label_query, input_query, label_fields, input_fields, label_field, input_field, label_name, input_name, label_size, input_size, label_sub_fields, input_sub_fields, label_mothod_type, input_mothod_type, label_pic_type, input_pic_type, input_modify_submit, input_delete_submit, form_end);
                $("select#mothod_type").find("#"+result.mothod_type).attr("selected","selected");
                $("select#pic_type").find("#"+result.pic_type).attr("selected","selected");
                $("#modify_button").click(function(){
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
                    $.ajax({
                        "type": "POST",
            		    "dataType": "json",
            		    "url": "/api/post_update_pic_profile",
            		    "data": update_data,
                        "success": function(result) {
                            if (result){
                                alert('修改成功！');
                                window.location.href='/manage_pic';
                            }
                        }
                    });
                });

                $("#delete_button").click(function(){
                    var delete_data = {
                        "id":$("#id").text()
                    };
                    $.ajax({
                        "type": "POST",
                        "dataType": "json",
                        "url": "/api/post_delete_pic_profile",
                        "data": delete_data,
                        "success": function(result) {
                            if (result){
                                alert('删除成功！');
                                window.location.href='/manage_pic';
                            }
                        }
                    });
                });
            }
        });
    });
});
