# sweep_login

## ���ذ�װ������
1. ʹ��pip��װ

```
pip install -r requirements.txt
```

## ��������
ֱ��ͬʱ����api_server.py��gevent_websocket_api.py�ļ�����

## ���ɻ���

```
�Ҹ���ʹ�õ���python��supervisor + gunicorn����
��supervisor�����ļ�����������������м��ɣ�Ŀ¼��ͬ��ֱ�Ӹ���

[program:generate_qcore]
command=/home/xlchen/python/bin/gunicorn --workers=2 -k gevent --pythonpath /home/xlchen/sweep_login --bind=0.0.0.0:8088 api_server:app

[program:sweep_api]
command=/home/xlchen/python/bin/gunicorn --workers=2 --pythonpath /home/xlchen/sweep_login -k "geventwebsocket.gunicorn.workers.GeventWebSocketWorker" -b 0.0.0.0:8080 gevent_websocket_api:web_socket_app
```


