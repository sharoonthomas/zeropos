"""
A flask based web application that listens to
printing requests and serves them
"""
import thread

import flask
from gevent.wsgi import WSGIServer

# A threadsafe lock to prevent two requests printing simultaneously
print_lock = thread.allocate_lock()


app = flask.Flask(__name__)


@app.route('/')
def home():
    return "Welcome to this web page"


@app.route('/print')
def print_handler():
    """
    A Handler that receives the ZPL in the body and sends it to the printer
    """
    with print_lock:
        # TODO: Print to the printer
        pass


if __name__ == '__main__':
    from config import CONFIG
    CONFIG.parse()

    local_ip = CONFIG['address']
    port = CONFIG['port']
    http_server = WSGIServer((local_ip, port), app)
    http_server.serve_forever()
