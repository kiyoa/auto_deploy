# sweep_login 扫码登录python实现

## 下载安装依赖库
1. 使用pip安装

```
pip install -r requirements.txt
```

## 调试运行
直接同时运行api_server.py、gevent_websocket_api.py文件即可

## 生成环境

```
我个人使用的是python的supervisor + gunicorn配置
在supervisor配置文件中添加如下内容运行即可，目录不同请直接更正

[program:generate_qcore]
command=/home/xlchen/python/bin/gunicorn --workers=2 -k gevent --pythonpath /home/xlchen/sweep_login --bind=0.0.0.0:8088 api_server:app

[program:sweep_api]
command=/home/xlchen/python/bin/gunicorn --workers=2 --pythonpath /home/xlchen/sweep_login -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" -b 0.0.0.0:8080 gevent_websocket_api:web_socket_app
```

# 注意： 登录进去的界面(index.heml)，没有进行认证，需要自己完善。


