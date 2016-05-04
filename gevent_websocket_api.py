# coding=utf-8


import redis
from gevent import pywsgi, sleep
from geventwebsocket.handler import WebSocketHandler


class WebSocketApp(object):
    '''Send random data to the websocket'''

    def __call__(self, environ, start_response):
        ws = environ['wsgi.websocket']
        r = redis.Redis(host='localhost', port=6379, db=0)
        message = ws.receive()
        r.setex(message, '', 60)
        while True:
            sleep(1)  # 阻塞
            end_flag = r.get(message)
            if end_flag is None:
                ws.close(code=1)
                break
            elif end_flag != '':
                ws.send("Your message was: %r, %s用户 登录成功即将跳转...." %
                        (message, r.get(message)))
                ws.close(code=0)
                break
        print u'请求结束'
web_socket_app = WebSocketApp()

if __name__ == '__main__':
    server = pywsgi.WSGIServer(
        ("", 8080), WebSocketApp(), handler_class=WebSocketHandler)
    server.serve_forever()
