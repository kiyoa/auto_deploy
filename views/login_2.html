<!DOCTYPE html>
<html>
<head>
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
  <script type="text/javascript">
    function b(){
     $("#auto_submit").submit();
    }
    var ws = new WebSocket("ws://{{ip}}:8080/websocket");
    ws.onopen = function() {
        only_flag = document.getElementById('image_id_flag');
        ws.send(only_flag.innerHTML);
    };
    ws.onmessage = function (evt) {
        console.log(evt.data);
        text_id = document.getElementById('h3_msg');
        text_id.innerHTML = evt.data;
        setTimeout("b()", 2000);
    };
    ws.onclose = function(evt) {
        if (evt.code == 666666){
            console.log(evt.code);
        }
        else {
            console.log(evt.code);
            console.log('二维码已过期，请刷新网页重新生成');
            var text_id = document.getElementById('h3_msg');
            text_id.innerHTML = '二维码已过期，请刷新网页重新生成';
        }
      };
  </script>
</head>
<h2>扫描二维码登录</h2>
<img src="{{url_add}}">
<a id="image_id_flag" hidden>{{flag}}</a>
<h3 id="h3_msg"></h3>
<form action="http://{{ip}}:8088/index" method="get" id="auto_submit">
    <input type="hidden" value=""/>
</form>
</body>
</html>