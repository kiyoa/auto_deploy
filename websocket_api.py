# coding=utf-8

import time
import redis
from my_config import IP
from bottle import request, Bottle, abort
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler


app = Bottle()


@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    try:
        message = wsock.receive()
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.setex(message, '', 10)
        while True:
            end_flag = r.get(message)
            if end_flag is None:
                wsock.close(code=1)
                break
            elif end_flag != '':
                wsock.send("Your message was: %r, %s用户 登录成功即将跳转...." % (message, r.get(message)))
                wsock.close(code=666666)
                break
            time.sleep(3)
    except WebSocketError:
        pass


# server = WSGIServer(("0.0.0.0", 8080), app, handler_class=WebSocketHandler)
server = WSGIServer((IP, 8080), app, handler_class=WebSocketHandler)
server.serve_forever()
# app.run(host="192.168.0.101", port='8080')
