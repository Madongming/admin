$(document).ready(function(){
    $("input:radio").click(function(){
        $("input[type='checkbox'][name='monitor_name']").each(function(){
            $(this).attr("checked", false);
            window.c=0;
        });
    });

    $("#conf_dashboard_yes").click(function(){
        if($("input[type='radio']:checked").val() ==='dashboard1'){
            if(window.c != 4){
                alert("选择的图表数目不是4！");
                return;
            }
            var checked_monitor_names = new Array(0,1,2,3);
            var input_num = '输入该图表要在面板上显示的序号：1~4';
            var isnotok = false;
            $("input[type='checkbox'][name='monitor_name']:checked").each(function(){
                if(isnotok){return;};
                var index = parseInt(prompt($(this).val(), input_num));
                if (index>4 || index<1){
                    alert("输入的序号超出范围，请重新提交，输入1～4的数字！");
                    checked_monitor_names = new Array(0,1,2,3);
                    isnotok = true;
                    return;
                };
                if (checked_monitor_names[index-1] != index-1){
                    alert("输入的序号重复！请重新提交！");
                    checked_monitor_names = new Array(0,1,2,3);
                    isnotok = true;
                    return;
                };
                checked_monitor_names[index-1]=$(this).val();
            });
            if(isnotok){return;};
            var data = {
                'dashboard1':checked_monitor_names
            };
            var url = '/dashboard1';
        };
        if($("input[type='radio']:checked").val() ==='dashboard2'){
            if(window.c != 3){
                alert("选择的图表数目不是3！");
                return;
            }
            var checked_monitor_names = new Array(0,1,2);
            var input_num = '输入该图表要在面板上显示的序号：1~3';
            var isnotok = false;
            $("input[type='checkbox'][name='monitor_name']:checked").each(function(){
                if(isnotok){return;};
                var index = parseInt(prompt($(this).val(), input_num));
                if (index>3 || index<1){
                    alert("输入的序号超出范围，请重新提交，输入1～3的数字！");
                    checked_monitor_names = new Array(0,1,2);
                    isnotok = true;
                    return;
                };
                if (checked_monitor_names[index-1] != index-1){
                    alert("输入的序号重复！请重新提交！");
                    checked_monitor_names = new Array(0,1,2);
                    isnotok = true;
                    return;
                };
                checked_monitor_names[index-1]=$(this).val();
            });
            if(isnotok){return;};
            var data = {
                'dashboard2':checked_monitor_names
            }
            var url = '/dashboard2';
        };
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": "/api/post_conf_dashboard",
            "data": data,
            "success": function(result) {
                if (result){
                    alert('设置成功！');
                    window.open(url, '_newtab');
                }
            }
        });
    });
});
