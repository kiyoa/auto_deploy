# coding=utf-8
import os
import qrcode
import random
import redis
from my_config import IP
from bottle import request, Bottle, static_file, template, TEMPLATE_PATH


HOME = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "views")) + '/')
app = Bottle()


@app.route('/update')
def update():
    r = redis.Redis(host='localhost', port=6379, db=0)
    user_id = request.GET.get('user_id')
    tmp_str = random.randint(900000, 999999)
    r.set(user_id, str(tmp_str))
    return u'授权成功'


@app.route("/")
def login():
    image_name = random.randint(100000, 999999999)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('http://%s:8088/update?user_id=%s' % (IP, image_name))
    qr.make(fit=True)
    img = qr.make_image()
    img.save('{0}/image/{1}.png'.format(HOME, image_name))
    return template('login', url_add='http://%s:8088/image?name=%s' % (IP, image_name), ip=IP, flag=image_name)


@app.route('/image')
def return_image():
    name = request.GET.get('name')
    dir_path = '%s/image/' % HOME
    return static_file('{}.png'.format(name), root=dir_path)


@app.error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'


@app.error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


@app.route('/index')
def return_image():
    return template('index')

if __name__ == '__main__':
    app.run(host=IP, port='8088', debug=True)
